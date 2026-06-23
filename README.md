# Watchr — Website Change Monitor

Real website monitoring app. Server actually fetches URLs and detects changes.

## Deploy FREE on Railway (5 minutes)

### Step 1 — GitHub pe upload karo
1. GitHub.com pe jaao → New repository banao → naam "watchr"
2. Ye saari files upload karo (app.py, requirements.txt, Procfile, railway.toml, templates/ folder)

### Step 2 — Railway pe deploy karo
1. **railway.app** pe jaao → "Start a New Project"
2. "Deploy from GitHub repo" choose karo
3. Apna "watchr" repo select karo
4. Railway automatically detect karega aur deploy kar dega
5. "Generate Domain" click karo → aapko ek free URL milega jaise: `watchr-abc123.up.railway.app`

**Done!** Ab koi bhi URL monitor kar sako real-time mein.

---

## Deploy FREE on Render (alternative)

1. **render.com** pe jaao → New → Web Service
2. GitHub repo connect karo
3. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Free plan choose karo → Deploy

---

## Local pe test karna

```bash
pip install -r requirements.txt
python app.py
# Open: http://localhost:5000
```

## Features
- ✅ Real URL fetching (server-side, no CORS issues)
- ✅ Text diff — exactly kya badla yeh dikhata hai
- ✅ Auto background checks (frequency ke hisaab se)
- ✅ Pause/Resume monitors
- ✅ Activity feed
- ✅ 25 monitors free
- ✅ Data file mein save hota hai (monitors.json)

## File Structure
```
watchr/
├── app.py              ← Flask backend
├── requirements.txt    ← Python packages
├── Procfile            ← Server start command
├── railway.toml        ← Railway config
├── monitors.json       ← Data (auto-created)
└── templates/
    └── index.html      ← Frontend UI
```
