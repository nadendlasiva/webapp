from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Task Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f0f4f8;
            min-height: 100vh;
        }

        .header {
            background: linear-gradient(135deg, #0078d4, #005a9e);
            color: white;
            padding: 24px 40px;
            display: flex;
            align-items: center;
            gap: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .header-icon { font-size: 40px; }
        .header h1 { font-size: 26px; font-weight: 700; }
        .header p { font-size: 14px; opacity: 0.85; margin-top: 4px; }

        .manager-section {
            display: flex;
            justify-content: center;
            margin: 30px 40px 10px;
        }
        .manager-card {
            background: linear-gradient(135deg, #0078d4, #005a9e);
            color: white;
            border-radius: 16px;
            padding: 20px 40px;
            display: flex;
            align-items: center;
            gap: 16px;
            box-shadow: 0 6px 20px rgba(0,120,212,0.35);
            min-width: 320px;
        }
        .manager-avatar {
            width: 56px; height: 56px;
            background: rgba(255,255,255,0.25);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 26px; font-weight: bold;
        }
        .manager-info h2 { font-size: 20px; font-weight: 700; }
        .manager-info p { font-size: 13px; opacity: 0.85; margin-top: 3px; }
        .manager-badge {
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.4);
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 12px;
            margin-top: 6px;
            display: inline-block;
        }

        .arrow-section {
            text-align: center;
            font-size: 28px;
            color: #0078d4;
            margin: 8px 0;
            animation: bounce 1.5s infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(6px); }
        }

        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 16px 40px;
            flex-wrap: wrap;
        }
        .stat-card {
            background: white;
            border-radius: 12px;
            padding: 14px 28px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            min-width: 130px;
        }
        .stat-card .number { font-size: 28px; font-weight: 700; color: #0078d4; }
        .stat-card .label { font-size: 12px; color: #666; margin-top: 4px; }

        .team-section {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin: 20px 40px 40px;
        }
        .member-column {
            background: white;
            border-radius: 16px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
            overflow: hidden;
        }
        .member-header {
            padding: 18px 20px;
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .member-header.akshay { background: linear-gradient(135deg, #107c10, #0b5e0b); }
        .member-header.lenin  { background: linear-gradient(135deg, #8764b8, #5c2d91); }
        .member-header.siva   { background: linear-gradient(135deg, #d83b01, #a52d01); }

        .member-avatar {
            width: 46px; height: 46px;
            background: rgba(255,255,255,0.25);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 20px; font-weight: bold; color: white;
        }
        .member-name { color: white; font-size: 17px; font-weight: 700; }
        .member-role { color: rgba(255,255,255,0.8); font-size: 12px; margin-top: 2px; }

        .tasks-list { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
        .task-card {
            border: 1px solid #e8ecf0;
            border-radius: 10px;
            padding: 14px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .task-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .task-title { font-size: 13px; font-weight: 600; color: #1a1a1a; margin-bottom: 10px; }
        .task-meta { display: flex; flex-direction: column; gap: 6px; }
        .task-row { display: flex; justify-content: space-between; align-items: center; font-size: 11px; }
        .task-row .key { color: #888; }

        .badge { padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
        .badge.completed  { background: #dff6dd; color: #107c10; }
        .badge.inprogress { background: #fff4ce; color: #835b00; }
        .badge.delayed    { background: #fde7e9; color: #c50f1f; }

        .risk { padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 600; }
        .risk.low    { background: #dff6dd; color: #107c10; }
        .risk.medium { background: #fff4ce; color: #835b00; }
        .risk.high   { background: #fde7e9; color: #c50f1f; }

        .date { color: #0078d4; font-weight: 600; }
        .dependency { color: #605e5c; font-style: italic; font-size: 11px; }

        .progress-bar {
            height: 4px;
            background: #e8ecf0;
            border-radius: 4px;
            margin-top: 10px;
            overflow: hidden;
        }
        .progress-fill { height: 100%; border-radius: 4px; }
        .fill-green  { background: #107c10; width: 100%; }
        .fill-yellow { background: #f0c400; }
        .fill-red    { background: #c50f1f; }

        footer {
            text-align: center;
            padding: 20px;
            color: #888;
            font-size: 12px;
            border-top: 1px solid #e0e0e0;
            background: white;
        }
    </style>
</head>
<body>

<div class="header">
    <div class="header-icon">☁️</div>
    <div>
        <h1>Azure Team Task Dashboard</h1>
        <p>Real-time task tracking | ERIKS IoT Project</p>
    </div>
</div>

<div class="manager-section">
    <div class="manager-card">
        <div class="manager-avatar">V</div>
        <div class="manager-info">
            <h2>Vivek R</h2>
            <p>Project Manager — Assigning & Tracking Tasks</p>
            <span class="manager-badge">👑 Manager</span>
        </div>
    </div>
</div>

<div class="arrow-section">⬇️ Assigning Tasks ⬇️</div>

<div class="stats-bar">
    <div class="stat-card"><div class="number">9</div><div class="label">Total Tasks</div></div>
    <div class="stat-card"><div class="number" style="color:#107c10">3</div><div class="label">Completed</div></div>
    <div class="stat-card"><div class="number" style="color:#835b00">4</div><div class="label">In Progress</div></div>
    <div class="stat-card"><div class="number" style="color:#c50f1f">2</div><div class="label">Delayed</div></div>
</div>

<div class="team-section">

    <div class="member-column">
        <div class="member-header akshay">
            <div class="member-avatar">A</div>
            <div><div class="member-name">Akshay</div><div class="member-role">Azure Infrastructure</div></div>
        </div>
        <div class="tasks-list">
            <div class="task-card">
                <div class="task-title">🔧 Azure Role Assignment Audit</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge completed">✅ Completed</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">20 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk low">Low</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">None</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-green"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">🔐 Service Principal Review</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge inprogress">🔄 In Progress</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">28 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk medium">Medium</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">Role Assignment Audit</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-yellow" style="width:60%"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">📊 Subscription Access Report</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge delayed">⚠️ Delayed</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">25 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk high">High</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">SP Review</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-red" style="width:30%"></div></div>
            </div>
        </div>
    </div>

    <div class="member-column">
        <div class="member-header lenin">
            <div class="member-avatar">L</div>
            <div><div class="member-name">Lenin</div><div class="member-role">DevOps & CI/CD</div></div>
        </div>
        <div class="tasks-list">
            <div class="task-card">
                <div class="task-title">⚙️ Azure DevOps Pipeline Setup</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge completed">✅ Completed</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">18 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk low">Low</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">None</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-green"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">🚀 Web App Deployment</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge inprogress">🔄 In Progress</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">30 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk medium">Medium</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">Pipeline Setup</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-yellow" style="width:70%"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">🔍 Monitoring & Alerts Config</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge inprogress">🔄 In Progress</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">05 Jul 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk low">Low</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">Web App Deployment</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-yellow" style="width:40%"></div></div>
            </div>
        </div>
    </div>

    <div class="member-column">
        <div class="member-header siva">
            <div class="member-avatar">S</div>
            <div><div class="member-name">Siva</div><div class="member-role">Security & Compliance</div></div>
        </div>
        <div class="tasks-list">
            <div class="task-card">
                <div class="task-title">🛡️ IAM Policy Review</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge completed">✅ Completed</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">22 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk low">Low</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">None</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-green"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">🔒 Security Compliance Audit</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge inprogress">🔄 In Progress</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">02 Jul 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk medium">Medium</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">IAM Policy Review</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-yellow" style="width:50%"></div></div>
            </div>
            <div class="task-card">
                <div class="task-title">📋 Access Control Documentation</div>
                <div class="task-meta">
                    <div class="task-row"><span class="key">Status</span><span class="badge delayed">⚠️ Delayed</span></div>
                    <div class="task-row"><span class="key">Due Date</span><span class="date">24 Jun 2026</span></div>
                    <div class="task-row"><span class="key">Risk</span><span class="risk high">High</span></div>
                    <div class="task-row"><span class="key">Dependency</span><span class="dependency">Security Audit</span></div>
                </div>
                <div class="progress-bar"><div class="progress-fill fill-red" style="width:20%"></div></div>
            </div>
        </div>
    </div>

</div>

<footer>
    Deployed via Azure DevOps | ERIKS IoT Project | Version 4.0 | Manager: Vivek R
</footer>

</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "4.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)