HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Watchr — Website Change Monitor</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
  :root {
    --ink:#0d0f12;--ink-muted:#5a6070;--ink-faint:#9aa0ad;
    --surface:#f7f8fa;--raised:#fff;--overlay:#f0f2f5;--border:#e3e6ec;
    --accent:#2563eb;--accent-light:#dbeafe;--accent-glow:rgba(37,99,235,.12);
    --green:#16a34a;--green-light:#dcfce7;
    --amber:#d97706;--amber-light:#fef3c7;
    --red:#dc2626;--red-light:#fee2e2;
    --r:10px;--rs:6px;
    --sh:0 1px 3px rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.04);
    --sh2:0 4px 12px rgba(0,0,0,.08),0 2px 4px rgba(0,0,0,.04);
    --sh3:0 12px 32px rgba(0,0,0,.1),0 4px 8px rgba(0,0,0,.06);
  }
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Inter',sans-serif;background:var(--surface);color:var(--ink);min-height:100vh;font-size:14px;line-height:1.5}
  .app{display:flex;min-height:100vh}

  /* SIDEBAR */
  .sidebar{width:220px;flex-shrink:0;background:var(--raised);border-right:1px solid var(--border);display:flex;flex-direction:column;padding:20px 0;position:fixed;top:0;left:0;bottom:0;z-index:10}
  .sb-logo{padding:0 20px 24px;display:flex;align-items:center;gap:10px;border-bottom:1px solid var(--border);margin-bottom:16px}
  .logo-mark{width:30px;height:30px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:16px}
  .logo-name{font-size:18px;font-weight:700;letter-spacing:-.5px}
  .nav{padding:0 12px;flex:1}
  .nav-label{font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.8px;color:var(--ink-faint);padding:4px 8px 8px}
  .nav-item{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:var(--rs);color:var(--ink-muted);cursor:pointer;font-size:13.5px;font-weight:500;transition:all .15s;margin-bottom:1px;border:none;background:none;width:100%;text-align:left;font-family:inherit}
  .nav-item:hover{background:var(--overlay);color:var(--ink)}
  .nav-item.active{background:var(--accent-light);color:var(--accent)}
  .sb-foot{padding:16px 20px 0;border-top:1px solid var(--border);margin-top:auto}
  .plan-badge{background:var(--overlay);border-radius:var(--rs);padding:10px 12px}
  .plan-name{font-weight:600;font-size:12px}
  .plan-usage{font-size:11px;color:var(--ink-muted);margin-top:4px}
  .usage-bar{height:3px;background:var(--border);border-radius:99px;margin-top:6px;overflow:hidden}
  .usage-fill{height:100%;background:var(--accent);border-radius:99px;transition:width .4s}

  /* MAIN */
  .main{margin-left:220px;flex:1;display:flex;flex-direction:column}
  .topbar{background:var(--raised);border-bottom:1px solid var(--border);padding:0 28px;height:56px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:9}
  .topbar-title{font-size:15px;font-weight:600}
  .topbar-actions{display:flex;gap:8px;align-items:center}
  .live-dot{width:8px;height:8px;border-radius:50%;background:var(--green);animation:pulse-g 2s infinite;flex-shrink:0}
  @keyframes pulse-g{0%,100%{box-shadow:0 0 0 0 rgba(22,163,74,.4)}50%{box-shadow:0 0 0 5px rgba(22,163,74,0)}}
  .live-label{font-size:11px;color:var(--green);font-weight:600}
  .content{padding:28px;flex:1}

  /* BUTTONS */
  .btn{display:inline-flex;align-items:center;gap:6px;padding:7px 14px;border-radius:var(--rs);font-size:13px;font-weight:500;cursor:pointer;border:none;transition:all .15s;font-family:inherit}
  .btn-primary{background:var(--accent);color:#fff}
  .btn-primary:hover{background:#1d4ed8}
  .btn-secondary{background:var(--overlay);color:var(--ink);border:1px solid var(--border)}
  .btn-secondary:hover{background:var(--border)}
  .btn-ghost{background:transparent;color:var(--ink-muted);border:1px solid transparent;padding:5px 8px}
  .btn-ghost:hover{background:var(--overlay);color:var(--ink)}
  .btn-sm{padding:5px 10px;font-size:12px}

  /* STATS */
  .stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
  .stat-card{background:var(--raised);border:1px solid var(--border);border-radius:var(--r);padding:18px 20px;box-shadow:var(--sh)}
  .stat-label{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.6px;color:var(--ink-faint);margin-bottom:8px}
  .stat-value{font-size:28px;font-weight:700;letter-spacing:-1px;color:var(--ink);line-height:1}
  .stat-sub{font-size:11px;color:var(--ink-muted);margin-top:4px}
  .stat-card.accent{border-color:var(--accent);background:linear-gradient(135deg,var(--accent-light),#fff)}
  .stat-card.accent .stat-value{color:var(--accent)}

  /* ADD CARD */
  .add-card{background:var(--raised);border:2px dashed var(--border);border-radius:var(--r);padding:20px 24px;margin-bottom:24px;transition:border-color .2s}
  .add-card:focus-within{border-color:var(--accent);border-style:solid}
  .add-card-title{font-size:13px;font-weight:600;margin-bottom:12px}
  .add-row{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap}
  .field{display:flex;flex-direction:column;gap:5px}
  .field label{font-size:11px;font-weight:600;color:var(--ink-muted);text-transform:uppercase;letter-spacing:.5px}
  .input{padding:8px 12px;border:1px solid var(--border);border-radius:var(--rs);font-family:inherit;font-size:13px;color:var(--ink);background:var(--raised);outline:none;transition:border-color .15s,box-shadow .15s}
  .input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-glow)}
  .url-input{width:320px;font-family:'DM Mono',monospace;font-size:12px}
  select.input{cursor:pointer;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%235a6070' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 10px center;padding-right:28px}

  /* TABLE HEADER */
  .table-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
  .table-title{font-size:14px;font-weight:600}
  .table-count{font-size:12px;color:var(--ink-muted);background:var(--overlay);padding:2px 8px;border-radius:99px;margin-left:8px}
  .filter-tabs{display:flex;gap:2px;background:var(--overlay);padding:3px;border-radius:var(--rs)}
  .filter-tab{padding:4px 12px;border-radius:4px;font-size:12px;font-weight:500;cursor:pointer;color:var(--ink-muted);transition:all .15s;border:none;background:none;font-family:inherit}
  .filter-tab.active{background:var(--raised);color:var(--ink);box-shadow:var(--sh)}

  /* MONITOR CARDS */
  .monitors-list{display:flex;flex-direction:column;gap:8px}
  .monitor-card{background:var(--raised);border:1px solid var(--border);border-radius:var(--r);padding:14px 18px;display:flex;align-items:center;gap:14px;box-shadow:var(--sh);transition:box-shadow .15s,border-color .15s;cursor:pointer;position:relative;overflow:hidden}
  .monitor-card:hover{box-shadow:var(--sh2);border-color:#c8cdd8}
  .monitor-card.changed{border-left:3px solid var(--amber)}
  .monitor-card.error{border-left:3px solid var(--red)}
  .monitor-card.checking{border-left:3px solid var(--accent)}
  .status-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
  .status-dot.ok{background:var(--green);box-shadow:0 0 0 3px var(--green-light)}
  .status-dot.changed{background:var(--amber);box-shadow:0 0 0 3px var(--amber-light);animation:pa 2s infinite}
  .status-dot.error{background:var(--red);box-shadow:0 0 0 3px var(--red-light)}
  .status-dot.checking{background:var(--accent);box-shadow:0 0 0 3px var(--accent-light);animation:pb 1.5s infinite}
  .status-dot.paused{background:var(--ink-faint)}
  @keyframes pa{0%,100%{box-shadow:0 0 0 3px var(--amber-light)}50%{box-shadow:0 0 0 5px rgba(217,119,6,.15)}}
  @keyframes pb{0%,100%{box-shadow:0 0 0 3px var(--accent-light)}50%{box-shadow:0 0 0 5px var(--accent-glow)}}
  .monitor-info{flex:1;min-width:0}
  .monitor-name{font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .monitor-url{font-size:11px;color:var(--ink-faint);font-family:'DM Mono',monospace;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px}
  .monitor-meta{display:flex;gap:16px;flex-shrink:0}
  .meta-item{text-align:right}
  .meta-label{font-size:10px;text-transform:uppercase;letter-spacing:.5px;color:var(--ink-faint);font-weight:600}
  .meta-value{font-size:12px;color:var(--ink-muted);margin-top:1px;font-weight:500}
  .monitor-badge{padding:3px 8px;border-radius:99px;font-size:11px;font-weight:600;flex-shrink:0}
  .monitor-badge.changed{background:var(--amber-light);color:var(--amber)}
  .monitor-badge.ok{background:var(--green-light);color:var(--green)}
  .monitor-badge.checking{background:var(--accent-light);color:var(--accent)}
  .monitor-badge.error{background:var(--red-light);color:var(--red)}
  .monitor-badge.paused{background:var(--overlay);color:var(--ink-faint)}
  .monitor-actions{display:flex;gap:4px;flex-shrink:0;opacity:0;transition:opacity .15s}
  .monitor-card:hover .monitor-actions{opacity:1}

  /* MODAL */
  .modal-overlay{position:fixed;inset:0;background:rgba(13,15,18,.5);backdrop-filter:blur(2px);z-index:100;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .2s}
  .modal-overlay.open{opacity:1;pointer-events:all}
  .modal{background:var(--raised);border-radius:14px;width:540px;max-width:95vw;max-height:85vh;overflow-y:auto;box-shadow:var(--sh3);transform:translateY(12px);transition:transform .2s;border:1px solid var(--border)}
  .modal-overlay.open .modal{transform:translateY(0)}
  .modal-header{padding:20px 24px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
  .modal-title{font-size:16px;font-weight:700;letter-spacing:-.3px}
  .modal-body{padding:20px 24px}
  .modal-footer{padding:16px 24px 20px;border-top:1px solid var(--border);display:flex;gap:8px;justify-content:flex-end}
  .close-btn{width:30px;height:30px;border-radius:6px;border:none;background:var(--overlay);cursor:pointer;display:flex;align-items:center;justify-content:center;color:var(--ink-muted);font-size:18px;line-height:1;transition:background .15s}
  .close-btn:hover{background:var(--border);color:var(--ink)}
  .form-grid{display:flex;flex-direction:column;gap:16px}
  .form-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}

  /* DIFF */
  .diff-viewer{background:#0d0f12;border-radius:var(--r);padding:16px;font-family:'DM Mono',monospace;font-size:12px;line-height:1.8;max-height:260px;overflow-y:auto;margin-top:12px}
  .diff-line{padding:1px 4px;border-radius:3px;white-space:pre-wrap;word-break:break-all}
  .diff-add{background:rgba(22,163,74,.2);color:#4ade80}
  .diff-remove{background:rgba(220,38,38,.2);color:#f87171}
  .diff-ctx{color:#6b7280}
  .diff-info{color:#60a5fa}

  /* BOTTOM */
  .section-2col{display:grid;grid-template-columns:1fr 360px;gap:20px;margin-top:24px}
  .card{background:var(--raised);border:1px solid var(--border);border-radius:var(--r);box-shadow:var(--sh)}
  .card-header{padding:16px 20px;border-bottom:1px solid var(--border);font-size:13px;font-weight:600;display:flex;align-items:center;justify-content:space-between}
  .card-body{padding:16px 20px}
  .activity-item{padding:10px 0;border-bottom:1px solid var(--border);display:flex;gap:10px;align-items:flex-start}
  .activity-item:last-child{border-bottom:none}
  .activity-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:5px}
  .activity-content{font-size:12.5px}
  .activity-name{font-weight:600}
  .activity-time{font-size:11px;color:var(--ink-faint);margin-top:2px}

  /* TOAST */
  .toast-container{position:fixed;bottom:24px;right:24px;z-index:200;display:flex;flex-direction:column;gap:8px}
  .toast{background:var(--ink);color:#fff;padding:12px 16px;border-radius:var(--r);font-size:13px;font-weight:500;box-shadow:var(--sh3);display:flex;align-items:center;gap:10px;animation:slideIn .25s ease-out;min-width:260px}
  .toast.success{background:var(--green)}
  .toast.warning{background:var(--amber)}
  .toast.error{background:var(--red)}
  @keyframes slideIn{from{transform:translateX(80px);opacity:0}to{transform:translateX(0);opacity:1}}

  /* EMPTY */
  .empty-state{text-align:center;padding:48px 24px;color:var(--ink-muted)}
  .empty-icon{font-size:40px;margin-bottom:12px;opacity:.5}
  .empty-title{font-size:15px;font-weight:600;color:var(--ink);margin-bottom:4px}

  /* LOADING */
  .spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite}
  @keyframes spin{to{transform:rotate(360deg)}}

  @media(max-width:900px){.sidebar{display:none}.main{margin-left:0}.stats-grid{grid-template-columns:repeat(2,1fr)}.section-2col{grid-template-columns:1fr}.url-input{width:100%}.add-row{flex-direction:column;align-items:stretch}}
</style>
</head>
<body>
<div class="app">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="sb-logo">
      <div class="logo-mark">👁</div>
      <div class="logo-name">Watchr</div>
    </div>
    <nav class="nav">
      <div class="nav-label">Monitor</div>
      <button class="nav-item active">⊞ Dashboard</button>
      <button class="nav-item" onclick="setFilter('changed',this);this.classList.add('active')">
        ⚡ Changes
        <span id="changes-badge" style="margin-left:auto;background:var(--amber);color:white;font-size:10px;font-weight:700;padding:1px 6px;border-radius:99px;display:none">0</span>
      </button>
      <button class="nav-item" onclick="setFilter('ok',this)">✓ All Clear</button>
      <button class="nav-item" onclick="setFilter('paused',this)">⏸ Paused</button>
    </nav>
    <div class="sb-foot">
      <div class="plan-badge">
        <div class="plan-name">Free Plan</div>
        <div class="plan-usage" id="sidebar-usage">0 / 25 monitors</div>
        <div class="usage-bar"><div class="usage-fill" id="usage-fill" style="width:0%"></div></div>
      </div>
    </div>
  </aside>

  <!-- MAIN -->
  <div class="main">
    <div class="topbar">
      <div style="display:flex;align-items:center;gap:10px">
        <div class="topbar-title">Dashboard</div>
        <div class="live-dot"></div>
        <div class="live-label">Live</div>
      </div>
      <div class="topbar-actions">
        <button class="btn btn-secondary btn-sm" onclick="checkAll()">🔄 Check All</button>
        <button class="btn btn-primary btn-sm" onclick="openModal('add-modal')">＋ Add Monitor</button>
      </div>
    </div>

    <div class="content">
      <!-- STATS -->
      <div class="stats-grid">
        <div class="stat-card accent">
          <div class="stat-label">Total Monitors</div>
          <div class="stat-value" id="stat-total">0</div>
          <div class="stat-sub">Tracked pages</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Changes Found</div>
          <div class="stat-value" id="stat-changes">0</div>
          <div class="stat-sub">Unread updates</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Currently OK</div>
          <div class="stat-value" id="stat-ok">0</div>
          <div class="stat-sub">No changes</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Errors</div>
          <div class="stat-value" id="stat-errors">0</div>
          <div class="stat-sub">Unreachable URLs</div>
        </div>
      </div>

      <!-- ADD -->
      <div class="add-card">
        <div class="add-card-title">＋ Quick Add Monitor</div>
        <div class="add-row">
          <div class="field">
            <label>Page URL</label>
            <input id="url-input" class="input url-input" type="url" placeholder="https://example.com/page" />
          </div>
          <div class="field">
            <label>Name (optional)</label>
            <input id="name-input" class="input" style="width:170px" type="text" placeholder="My monitor" />
          </div>
          <div class="field">
            <label>Check Every</label>
            <select id="freq-input" class="input" style="width:130px">
              <option value="5m">5 minutes</option>
              <option value="15m" selected>15 minutes</option>
              <option value="1h">1 hour</option>
              <option value="6h">6 hours</option>
              <option value="1d">Daily</option>
            </select>
          </div>
          <button class="btn btn-primary" id="add-btn" onclick="addMonitor()">Add Monitor</button>
        </div>
      </div>

      <!-- MONITORS -->
      <div class="table-header">
        <div style="display:flex;align-items:center;gap:8px">
          <div class="table-title">Monitors</div>
          <span class="table-count" id="monitor-count">0</span>
        </div>
        <div class="filter-tabs">
          <button class="filter-tab active" onclick="setFilter('all',this)">All</button>
          <button class="filter-tab" onclick="setFilter('changed',this)">Changed</button>
          <button class="filter-tab" onclick="setFilter('ok',this)">OK</button>
          <button class="filter-tab" onclick="setFilter('error',this)">Errors</button>
        </div>
      </div>
      <div class="monitors-list" id="monitors-list"></div>

      <!-- BOTTOM -->
      <div class="section-2col">
        <div class="card">
          <div class="card-header">
            Recent Activity
            <span id="activity-count" style="font-size:11px;color:var(--ink-faint);font-weight:400"></span>
          </div>
          <div class="card-body" id="activity-feed" style="max-height:320px;overflow-y:auto">
            <div style="color:var(--ink-faint);font-size:12px;text-align:center;padding:24px 0">No activity yet.</div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">How It Works</div>
          <div class="card-body" style="display:flex;flex-direction:column;gap:14px;font-size:13px">
            <div style="display:flex;gap:12px;align-items:flex-start">
              <div style="width:24px;height:24px;background:var(--accent-light);color:var(--accent);border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;flex-shrink:0">1</div>
              <div><div style="font-weight:600">Add a URL</div><div style="color:var(--ink-muted);font-size:12px;margin-top:2px">Paste any public webpage URL you want to watch</div></div>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start">
              <div style="width:24px;height:24px;background:var(--accent-light);color:var(--accent);border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;flex-shrink:0">2</div>
              <div><div style="font-weight:600">We fetch it live</div><div style="color:var(--ink-muted);font-size:12px;margin-top:2px">Server fetches the real page and stores a snapshot</div></div>
            </div>
            <div style="display:flex;gap:12px;align-items:flex-start">
              <div style="width:24px;height:24px;background:var(--accent-light);color:var(--accent);border-radius:6px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;flex-shrink:0">3</div>
              <div><div style="font-weight:600">Change detected</div><div style="color:var(--ink-muted);font-size:12px;margin-top:2px">Diff is shown here every time content changes</div></div>
            </div>
            <div style="background:var(--overlay);border-radius:var(--rs);padding:10px 12px;font-size:11px;color:var(--ink-muted)">
              ⚡ Checks run on the server — no browser needed to stay open
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ADD MODAL -->
<div class="modal-overlay" id="add-modal">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">Add New Monitor</div>
      <button class="close-btn" onclick="closeModal('add-modal')">×</button>
    </div>
    <div class="modal-body">
      <div class="form-grid">
        <div class="field">
          <label>Page URL *</label>
          <input id="m-url" class="input" type="url" placeholder="https://example.com/page-to-watch" />
        </div>
        <div class="field">
          <label>Monitor Name</label>
          <input id="m-name" class="input" type="text" placeholder="e.g. AWS Pricing Page" />
        </div>
        <div class="form-row">
          <div class="field">
            <label>Check Frequency</label>
            <select id="m-freq" class="input">
              <option value="5m">Every 5 minutes</option>
              <option value="15m" selected>Every 15 minutes</option>
              <option value="1h">Every hour</option>
              <option value="6h">Every 6 hours</option>
              <option value="1d">Daily</option>
            </select>
          </div>
          <div class="field">
            <label>Tags</label>
            <input id="m-tags" class="input" type="text" placeholder="pricing, news, competitor" />
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary" onclick="closeModal('add-modal')">Cancel</button>
      <button class="btn btn-primary" onclick="addMonitorFull()">Start Monitoring</button>
    </div>
  </div>
</div>

<!-- DETAIL MODAL -->
<div class="modal-overlay" id="detail-modal">
  <div class="modal">
    <div class="modal-header">
      <div>
        <div class="modal-title" id="d-title">Monitor Details</div>
        <div style="font-size:11px;color:var(--ink-faint);margin-top:2px;font-family:'DM Mono',monospace" id="d-url"></div>
      </div>
      <button class="close-btn" onclick="closeModal('detail-modal')">×</button>
    </div>
    <div class="modal-body">
      <div style="display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap">
        <div class="stat-card" style="flex:1;min-width:110px;padding:12px 14px">
          <div class="stat-label">Status</div>
          <div class="stat-value" id="d-status" style="font-size:18px">—</div>
        </div>
        <div class="stat-card" style="flex:1;min-width:110px;padding:12px 14px">
          <div class="stat-label">Last Checked</div>
          <div class="stat-value" id="d-checked" style="font-size:13px;letter-spacing:0;line-height:1.3">—</div>
        </div>
        <div class="stat-card" style="flex:1;min-width:110px;padding:12px 14px">
          <div class="stat-label">Total Changes</div>
          <div class="stat-value" id="d-changes" style="font-size:18px">0</div>
        </div>
      </div>
      <div style="font-size:13px;font-weight:600;margin-bottom:6px">Latest Diff</div>
      <div class="diff-viewer" id="d-diff">
        <div class="diff-ctx">// No changes detected yet.</div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary" id="d-pause-btn" onclick="togglePauseFromDetail()">Pause</button>
      <button class="btn btn-secondary" onclick="checkNowDetail()">🔄 Check Now</button>
      <button class="btn btn-primary" onclick="closeModal('detail-modal')">Done</button>
    </div>
  </div>
</div>

<div class="toast-container" id="toast-container"></div>

<script>
let monitors = [], activity = [], currentDetailId = null, filterMode = 'all';

// ── API ──
async function api(path, method='GET', body=null) {
  const opts = { method, headers: {'Content-Type':'application/json'} };
  if (body) opts.body = JSON.stringify(body);
  const r = await fetch('/api' + path, opts);
  return r.json();
}

async function load() {
  const data = await api('/monitors');
  monitors = data.monitors || [];
  activity = data.activity || [];
  render();
}

async function addMonitor() {
  const url = document.getElementById('url-input').value.trim();
  const name = document.getElementById('name-input').value.trim();
  const freq = document.getElementById('freq-input').value;
  if (!url) { toast('Please enter a URL', 'error'); return; }
  const btn = document.getElementById('add-btn');
  btn.innerHTML = '<span class="spinner"></span> Adding…';
  btn.disabled = true;
  try {
    const m = await api('/monitors', 'POST', { url, name, freq });
    if (m.error) { toast(m.error, 'error'); return; }
    document.getElementById('url-input').value = '';
    document.getElementById('name-input').value = '';
    toast(`Monitoring started — first check in progress…`, 'success');
    await load();
  } finally {
    btn.innerHTML = 'Add Monitor';
    btn.disabled = false;
  }
}

async function addMonitorFull() {
  const url = document.getElementById('m-url').value.trim();
  const name = document.getElementById('m-name').value.trim();
  const freq = document.getElementById('m-freq').value;
  const tags = document.getElementById('m-tags').value.split(',').map(s=>s.trim()).filter(Boolean);
  if (!url) { toast('Please enter a URL', 'error'); return; }
  const m = await api('/monitors', 'POST', { url, name, freq, tags });
  if (m.error) { toast(m.error, 'error'); return; }
  closeModal('add-modal');
  toast(`Monitoring started — first check in progress…`, 'success');
  await load();
}

async function checkOne(id) {
  await api(`/monitors/${id}/check`, 'POST');
  toast('Checking now…', '');
  setTimeout(load, 3000);
  setTimeout(load, 8000);
}

async function checkAll() {
  for (const m of monitors.filter(m=>!m.paused)) {
    await api(`/monitors/${m.id}/check`, 'POST');
  }
  toast(`Checking ${monitors.filter(m=>!m.paused).length} monitors…`, '');
  setTimeout(load, 4000);
  setTimeout(load, 10000);
}

async function togglePause(id) {
  const r = await api(`/monitors/${id}/pause`, 'POST');
  toast(r.paused ? 'Monitor paused' : 'Monitor resumed', 'success');
  await load();
}

async function deleteMonitor(id) {
  if (!confirm('Delete this monitor?')) return;
  await api(`/monitors/${id}`, 'DELETE');
  toast('Monitor deleted', '');
  await load();
}

// ── RENDER ──
function render() {
  const changed = monitors.filter(m=>m.status==='changed').length;
  const ok = monitors.filter(m=>m.status==='ok').length;
  const errors = monitors.filter(m=>m.status==='error').length;
  document.getElementById('stat-total').textContent = monitors.length;
  document.getElementById('stat-changes').textContent = changed;
  document.getElementById('stat-ok').textContent = ok;
  document.getElementById('stat-errors').textContent = errors;
  document.getElementById('monitor-count').textContent = monitors.length;
  const badge = document.getElementById('changes-badge');
  badge.textContent = changed; badge.style.display = changed > 0 ? '' : 'none';
  const pct = Math.round(monitors.length/25*100);
  document.getElementById('sidebar-usage').textContent = `${monitors.length} / 25 monitors`;
  document.getElementById('usage-fill').style.width = pct + '%';
  renderMonitors(); renderActivity();
}

function renderMonitors() {
  const list = document.getElementById('monitors-list');
  let filtered = monitors;
  if (filterMode==='changed') filtered = monitors.filter(m=>m.status==='changed');
  else if (filterMode==='ok') filtered = monitors.filter(m=>m.status==='ok');
  else if (filterMode==='paused') filtered = monitors.filter(m=>m.paused);
  else if (filterMode==='error') filtered = monitors.filter(m=>m.status==='error');

  if (filtered.length === 0) {
    list.innerHTML = `<div class="empty-state"><div class="empty-icon">◉</div><div class="empty-title">No monitors here</div><div style="font-size:13px">Add a URL above to start watching for changes.</div></div>`;
    return;
  }
  list.innerHTML = filtered.map(m => {
    const sc = m.paused ? 'paused' : (m.status||'checking');
    const badge = m.paused ? 'Paused' : sc==='changed' ? '⚡ Changed' : sc==='checking' ? '🔄 Checking…' : sc==='error' ? '⚠ Error' : '✓ OK';
    return `<div class="monitor-card ${m.paused?'':sc}" onclick="openDetail('${m.id}')">
      <div class="status-dot ${sc}"></div>
      <div class="monitor-info">
        <div class="monitor-name">${m.name}</div>
        <div class="monitor-url">${m.url}</div>
      </div>
      <div class="monitor-meta">
        <div class="meta-item"><div class="meta-label">Frequency</div><div class="meta-value">${freqLabel(m.freq)}</div></div>
        <div class="meta-item"><div class="meta-label">Last Check</div><div class="meta-value">${m.lastChecked ? timeAgo(m.lastChecked) : 'Pending'}</div></div>
        <div class="meta-item"><div class="meta-label">Changes</div><div class="meta-value">${m.changesCount||0}</div></div>
      </div>
      <span class="monitor-badge ${sc}">${badge}</span>
      <div class="monitor-actions" onclick="event.stopPropagation()">
        <button class="btn btn-ghost btn-sm" title="Check now" onclick="checkOne('${m.id}')">🔄</button>
        <button class="btn btn-ghost btn-sm" title="${m.paused?'Resume':'Pause'}" onclick="togglePause('${m.id}')">${m.paused?'▶':'⏸'}</button>
        <button class="btn btn-ghost btn-sm" title="Delete" onclick="deleteMonitor('${m.id}')">🗑</button>
      </div>
    </div>`;
  }).join('');
}

function renderActivity() {
  const feed = document.getElementById('activity-feed');
  if (!activity.length) { feed.innerHTML = '<div style="color:var(--ink-faint);font-size:12px;text-align:center;padding:24px 0">No activity yet.</div>'; return; }
  const colorMap = {'changed':'var(--amber)','added':'var(--accent)','checked':'var(--green)','paused':'var(--ink-faint)'};
  feed.innerHTML = activity.slice(0,15).map(a=>`
    <div class="activity-item">
      <div class="activity-dot" style="background:${a.color||colorMap[a.type]||'var(--ink-faint)'}"></div>
      <div class="activity-content">
        <span class="activity-name">${a.name}</span> — ${a.type==='changed'?'content changed':a.type==='added'?'monitor added':a.type==='checked'?'checked, no change':'status changed'}
        <div class="activity-time">${timeAgo(a.time)}</div>
      </div>
    </div>`).join('');
  document.getElementById('activity-count').textContent = `${activity.length} events`;
}

// ── DETAIL ──
function openDetail(id) {
  currentDetailId = id;
  const m = monitors.find(m=>m.id===id);
  if (!m) return;
  document.getElementById('d-title').textContent = m.name;
  document.getElementById('d-url').textContent = m.url;
  document.getElementById('d-status').textContent = m.paused ? 'PAUSED' : (m.status||'').toUpperCase();
  document.getElementById('d-checked').textContent = m.lastChecked ? timeAgo(m.lastChecked) : 'Not yet';
  document.getElementById('d-changes').textContent = m.changesCount||0;
  document.getElementById('d-pause-btn').textContent = m.paused ? 'Resume' : 'Pause';
  const diff = document.getElementById('d-diff');
  if (m.lastDiff) {
    diff.innerHTML = m.lastDiff.split('\\n').map(line => {
      if (line.startsWith('+++') || line.startsWith('---')) return `<div class="diff-line diff-info">${esc(line)}</div>`;
      if (line.startsWith('+')) return `<div class="diff-line diff-add">${esc(line)}</div>`;
      if (line.startsWith('-')) return `<div class="diff-line diff-remove">${esc(line)}</div>`;
      if (line.startsWith('@@')) return `<div class="diff-line diff-info">${esc(line)}</div>`;
      return `<div class="diff-line diff-ctx">${esc(line)}</div>`;
    }).join('');
  } else {
    diff.innerHTML = `<div class="diff-ctx">// No changes detected yet.</div><div class="diff-ctx">// Status: ${m.status||'checking'}</div>`;
  }
  openModal('detail-modal');
}
function esc(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function togglePauseFromDetail() { if(currentDetailId){togglePause(currentDetailId);closeModal('detail-modal');} }
function checkNowDetail() { if(currentDetailId){closeModal('detail-modal');checkOne(currentDetailId);} }

// ── UI helpers ──
function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-overlay').forEach(el=>el.addEventListener('click',e=>{if(e.target===el)closeModal(el.id);}));

function setFilter(mode, el) {
  filterMode = mode;
  document.querySelectorAll('.filter-tab,.nav-item').forEach(t=>t.classList.remove('active'));
  if (el) el.classList.add('active');
  renderMonitors();
}

function toast(msg, type) {
  const c = document.getElementById('toast-container');
  const t = document.createElement('div');
  t.className = 'toast '+(type||'');
  t.textContent = msg;
  c.appendChild(t);
  setTimeout(()=>t.remove(), 4000);
}

function freqLabel(f) {
  return {'1m':'1 min','5m':'5 min','15m':'15 min','1h':'1 hr','6h':'6 hr','1d':'Daily'}[f]||f;
}

function timeAgo(iso) {
  if (!iso) return '—';
  const diff = (Date.now() - new Date(iso))/1000;
  if (diff < 60) return 'just now';
  if (diff < 3600) return Math.floor(diff/60)+'m ago';
  if (diff < 86400) return Math.floor(diff/3600)+'h ago';
  return Math.floor(diff/86400)+'d ago';
}

// Auto-refresh every 15s
load();
setInterval(load, 15000);
</script>
</body>
</html>
"""

import os, json, hashlib, time, threading, difflib, smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# ── Email Config ──
EMAIL_SENDER   = "slrewar007@gmail.com"
EMAIL_PASSWORD = "tzjynnailrrszrvf"
EMAIL_RECEIVER = "rewarshyam456@gmail.com"
METER_URL      = "https://tgnpdcl.bestinfra.app/mdm/ModemDetails.jsp?modem_sl_no=TGNP00106"

# ── Storage ──
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

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Watchr/1.0)"}

# ── Fetch meter data as table rows ──
def fetch_meter_data():
    try:
        r = requests.get(METER_URL, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(r.text, "html.parser")
        rows = {}
        for tr in soup.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) == 2:
                key = tds[0].get_text(strip=True)
                val = tds[1].get_text(strip=True)
                if key and val:
                    rows[key] = val
        return rows
    except Exception as e:
        return {"Error": str(e)}

# ── Send email ──
def send_email(subject, html_body):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = EMAIL_SENDER
        msg["To"]      = EMAIL_RECEIVER
        msg.attach(MIMEText(html_body, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(EMAIL_SENDER, EMAIL_PASSWORD)
            s.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print(f"[EMAIL] Sent: {subject}")
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False

# ── Build beautiful HTML email ──
def build_email_html(data, timestamp):
    rows_html = ""
    important = ["kWh(I)", "kVArh_Ld(I)", "kVArh_Lag(I)", "kVAh(I)",
                 "R-PH Voltage", "Y-PH Voltage", "B-PH Voltage",
                 "R-PH Current", "Y-PH Current", "B-PH Current",
                 "R-PH PF", "Y-PH PF", "B-PH PF", "Avg_PF",
                 "Modem Serial Number", "Meter Serial Number",
                 "Meter Date & Time", "Modem Date & Time", "Latest Alert"]
    # Show important rows first, then rest
    shown = set()
    for key in important:
        if key in data:
            val = data[key]
            color = "#fff8e1" if "Alert" in key else "#ffffff"
            rows_html += f'<tr style="background:{color}"><td style="padding:8px 14px;border-bottom:1px solid #eee;font-weight:600;color:#374151;width:45%">{key}</td><td style="padding:8px 14px;border-bottom:1px solid #eee;color:#111827">{val}</td></tr>'
            shown.add(key)
    for key, val in data.items():
        if key not in shown:
            rows_html += f'<tr><td style="padding:7px 14px;border-bottom:1px solid #f3f4f6;color:#6b7280;width:45%">{key}</td><td style="padding:7px 14px;border-bottom:1px solid #f3f4f6;color:#374151">{val}</td></tr>'

    return f"""
    <div style="font-family:Arial,sans-serif;max-width:620px;margin:0 auto;background:#f9fafb;padding:24px">
      <div style="background:#16a34a;border-radius:10px 10px 0 0;padding:20px 24px">
        <h2 style="color:white;margin:0;font-size:20px">⚡ Meter Hourly Snapshot</h2>
        <p style="color:#bbf7d0;margin:6px 0 0;font-size:13px">TGNP00106 — {timestamp}</p>
      </div>
      <div style="background:white;border-radius:0 0 10px 10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08)">
        <table style="width:100%;border-collapse:collapse">
          {rows_html}
        </table>
      </div>
      <p style="text-align:center;color:#9ca3af;font-size:11px;margin-top:16px">
        Sent by Watchr • {METER_URL[:60]}...
      </p>
    </div>"""

# ── Hourly meter email scheduler ──
def meter_email_scheduler():
    time.sleep(10)  # wait for server to start
    while True:
        now = datetime.now()
        print(f"[METER] Fetching at {now.strftime('%H:%M:%S')}")
        data = fetch_meter_data()
        timestamp = now.strftime("%d-%m-%Y %H:%M")
        subject = f"⚡ Meter Data — {timestamp} | kWh: {data.get('kWh(I)', 'N/A')}"
        html = build_email_html(data, timestamp)
        send_email(subject, html)
        # Sleep until next hour
        time.sleep(3600)

threading.Thread(target=meter_email_scheduler, daemon=True).start()

# ── General monitor fetch ──
def fetch_content(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator="\n", strip=True)
    except:
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
        m["contentHash"] = new_hash
        m["contentSnapshot"] = content[:3000]
        m["status"] = "ok"
    elif old_hash != new_hash:
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
        # Send change alert email
        subject = f"🔔 Change Detected: {m['name']}"
        html = f"""<div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto">
          <div style="background:#d97706;padding:20px;border-radius:10px 10px 0 0">
            <h2 style="color:white;margin:0">🔔 Change Detected!</h2>
            <p style="color:#fef3c7;margin:4px 0 0">{m['name']}</p>
          </div>
          <div style="background:white;padding:20px;border-radius:0 0 10px 10px">
            <p><b>URL:</b> {m['url']}</p>
            <p><b>Time:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}</p>
            <pre style="background:#1e1e2e;color:#cdd6f4;padding:16px;border-radius:8px;font-size:12px;overflow-x:auto">{m.get('lastDiff','No diff available')}</pre>
          </div>
        </div>"""
        send_email(subject, html)
    else:
        m["status"] = "ok"
    db["activity"] = db["activity"][:50]
    save_data(db)

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
    return Response(HTML, mimetype="text/html")

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

@app.route("/api/test-email", methods=["GET", "POST"])
def test_email():
    data = fetch_meter_data()
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
    subject = f"✅ Test Email — Meter Data {timestamp}"
    html = build_email_html(data, timestamp)
    ok = send_email(subject, html)
    return jsonify({"sent": ok})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
