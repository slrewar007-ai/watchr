import os, json, hashlib, time, threading, difflib
from datetime import datetime
from flask import Flask, jsonify, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# ── Storage (in-memory + file fallback) ──
DATA_FILE = "monitors.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"monitors": [], "activity": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

db = load_data()

# ── Fetch & compare ──
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Watchr/1.0)"}

def fetch_content(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        # Remove scripts/styles for clean text diff
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        return None

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest() if text else None

def check_monitor(m):
    content = fetch_content(m["url"])
    if content is None:
        m["status"] = "error"
        m["lastChecked"] = datetime.now().isoformat()
        return

    new_hash = get_hash(content)
    old_hash = m.get("contentHash")
    m["lastChecked"] = datetime.now().isoformat()

    if old_hash is None:
        # First check
        m["contentHash"] = new_hash
        m["contentSnapshot"] = content[:3000]
        m["status"] = "ok"
    elif old_hash != new_hash:
        # Changed!
        old_content = m.get("contentSnapshot", "")
        diff = list(difflib.unified_diff(
            old_content.splitlines()[:60],
            content.splitlines()[:60],
            lineterm="", n=2
        ))
        m["lastDiff"] = "\n".join(diff[:50])
        m["contentHash"] = new_hash
        m["contentSnapshot"] = content[:3000]
        m["status"] = "changed"
        m["changesCount"] = m.get("changesCount", 0) + 1
        m["history"] = ([datetime.now().isoformat()] + m.get("history", []))[:20]
        db["activity"].insert(0, {
            "type": "changed", "name": m["name"],
            "time": datetime.now().isoformat(), "color": "#d97706"
        })
    else:
        m["status"] = "ok"

    db["activity"] = db["activity"][:50]
    save_data(db)

# ── Background scheduler ──
def scheduler():
    while True:
        time.sleep(60)
        now = time.time()
        for m in db["monitors"]:
            if m.get("paused"):
                continue
            freq_map = {"1m":60,"5m":300,"15m":900,"1h":3600,"6h":21600,"1d":86400}
            freq_secs = freq_map.get(m.get("freq","15m"), 900)
            last = m.get("lastChecked")
            if last:
                last_ts = datetime.fromisoformat(last).timestamp()
                if now - last_ts < freq_secs:
                    continue
            check_monitor(m)

threading.Thread(target=scheduler, daemon=True).start()

# ── API Routes ──
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/monitors", methods=["GET"])
def get_monitors():
    return jsonify({"monitors": db["monitors"], "activity": db["activity"][:20]})

@app.route("/api/monitors", methods=["POST"])
def add_monitor():
    data = request.json
    url = data.get("url", "").strip()
    if not url or not url.startswith("http"):
        return jsonify({"error": "Invalid URL"}), 400
    if len(db["monitors"]) >= 25:
        return jsonify({"error": "Free plan limit: 25 monitors"}), 400

    m = {
        "id": hashlib.md5(f"{url}{time.time()}".encode()).hexdigest()[:10],
        "name": data.get("name") or url.split("/")[2],
        "url": url,
        "freq": data.get("freq", "15m"),
        "type": data.get("type", "full"),
        "status": "checking",
        "lastChecked": None,
        "contentHash": None,
        "contentSnapshot": None,
        "lastDiff": None,
        "changesCount": 0,
        "history": [],
        "paused": False,
        "tags": data.get("tags", [])
    }
    db["monitors"].insert(0, m)
    db["activity"].insert(0, {
        "type": "added", "name": m["name"],
        "time": datetime.now().isoformat(), "color": "#2563eb"
    })
    save_data(db)

    # Check immediately in background
    threading.Thread(target=lambda: check_monitor(m), daemon=True).start()
    return jsonify(m)

@app.route("/api/monitors/<mid>/check", methods=["POST"])
def check_now(mid):
    m = next((x for x in db["monitors"] if x["id"] == mid), None)
    if not m:
        return jsonify({"error": "Not found"}), 404
    m["status"] = "checking"
    threading.Thread(target=lambda: check_monitor(m), daemon=True).start()
    return jsonify({"ok": True})

@app.route("/api/monitors/<mid>/pause", methods=["POST"])
def pause_monitor(mid):
    m = next((x for x in db["monitors"] if x["id"] == mid), None)
    if not m:
        return jsonify({"error": "Not found"}), 404
    m["paused"] = not m.get("paused", False)
    save_data(db)
    return jsonify({"paused": m["paused"]})

@app.route("/api/monitors/<mid>", methods=["DELETE"])
def delete_monitor(mid):
    db["monitors"] = [x for x in db["monitors"] if x["id"] != mid]
    save_data(db)
    return jsonify({"ok": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
