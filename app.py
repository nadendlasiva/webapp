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
    <title>Azure Boards - Task Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8f9fa; min-height: 100vh; }
        .top-bar { background: #0078d4; color: white; padding: 10px 24px; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
        .page-header { padding: 20px 24px 12px; border-bottom: 1px solid #e0e0e0; background: white; display: flex; align-items: center; gap: 16px; }
        .manager-chip { display: flex; align-items: center; gap: 8px; background: #e6f1fb; border: 1px solid #b5d4f4; border-radius: 20px; padding: 6px 14px; }
        .avatar { width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; flex-shrink: 0; }
        .av-blue   { background: #b5d4f4; color: #0c447c; }
        .av-green  { background: #c0dd97; color: #27500a; }
        .av-purple { background: #cecbf6; color: #26215c; }
        .av-amber  { background: #fac775; color: #412402; }
        .manager-name { font-size: 13px; font-weight: 600; color: #0c447c; }
        .manager-role { font-size: 11px; color: #185fa5; }
        .arrow { font-size: 12px; color: #666; }
        .stats-bar { display: flex; gap: 12px; padding: 14px 24px; background: white; border-bottom: 1px solid #e0e0e0; flex-wrap: wrap; }
        .stat { background: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 8px; padding: 8px 20px; text-align: center; min-width: 90px; }
        .stat-num { font-size: 22px; font-weight: 600; color: #0078d4; }
        .stat-lbl { font-size: 11px; color: #666; margin-top: 2px; }
        .s-green { color: #107c10 !important; }
        .s-blue  { color: #0078d4 !important; }
        .s-red   { color: #c50f1f !important; }
        .board { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; padding: 20px 24px; }
        .column { background: white; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; }
        .col-header { padding: 12px 14px; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid #e0e0e0; }
        .col-akshay { border-top: 3px solid #107c10; }
        .col-lenin  { border-top: 3px solid #5c2d91; }
        .col-siva   { border-top: 3px solid #ca5010; }
        .col-name { font-size: 14px; font-weight: 600; color: #1a1a1a; }
        .col-role { font-size: 11px; color: #666; margin-top: 1px; }
        .task-badge { margin-left: auto; font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #f0f0f0; color: #333; }
        .tasks { padding: 12px; display: flex; flex-direction: column; gap: 10px; }
        .task-card { border: 1px solid #e0e0e0; border-radius: 6px; padding: 12px; background: #fafafa; transition: box-shadow 0.2s; }
        .task-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); background: white; }
        .task-id { font-size: 10px; color: #0078d4; font-weight: 600; margin-bottom: 4px; }
        .task-title { font-size: 13px; font-weight: 600; color: #1a1a1a; margin-bottom: 10px; line-height: 1.4; }
        .task-fields { border-top: 1px solid #f0f0f0; padding-top: 8px; display: flex; flex-direction: column; gap: 5px; }
        .field-row { display: flex; justify-content: space-between; align-items: center; }
        .field-key { font-size: 11px; color: #666; }
        .badge { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; }
        .b-done  { background: #dff6dd; color: #107c10; }
        .b-prog  { background: #cce4f7; color: #004f8c; }
        .b-delay { background: #fde7e9; color: #c50f1f; }
        .risk-low  { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #dff6dd; color: #107c10; }
        .risk-med  { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #fff4ce; color: #835b00; }
        .risk-high { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #fde7e9; color: #c50f1f; }
        .date-val { font-size: 11px; color: #0078d4; font-weight: 600; }
        .dep-val  { font-size: 10px; color: #666; font-style: italic; text-align: right; max-width: 120px; }
        .progress { height: 3px; background: #e0e0e0; border-radius: 2px; margin-top: 8px; }
        .prog-fill { height: 100%; border-radius: 2px; }
        .p-green { background: #107c10; width: 100%; }
        .p-blue  { background: #0078d4; }
        .p-red   { background: #c50f1f; }
        footer { text-align: center; padding: 16px; color: #888; font-size: 11px; border-top: 1px solid #e0e0e0; background: white; margin-top: 8px; }
    </style>
</head>
<body>

<div class="top-bar">
    &#9651; Azure Boards &nbsp;|&nbsp; ERIKS IoT Project
</div>

<div class="page-header">
    <div class="manager-chip">
        <div class="avatar av-blue">VR</div>
        <div>
            <div class="manager-name">Vivek R</div>
            <div class="manager-role">Project Manager</div>
        </div>
    </div>
    <div class="arrow">&#8594; Assigning tasks to team</div>
</div>

<div class="stats-bar">
    <div class="stat"><div class="stat-num">9</div><div class="stat-lbl">Total tasks</div></div>
    <div class="stat"><div class="stat-num s-green">3</div><div class="stat-lbl">Completed</div></div>
    <div class="stat"><div class="stat-num s-blue">4</div><div class="stat-lbl">In progress</div></div>
    <div class="stat"><div class="stat-num s-red">2</div><div class="stat-lbl">Delayed</div></div>
</div>

<div class="board">

    <!-- AKSHAY -->
    <div class="column col-akshay">
        <div class="col-header">
            <div class="avatar av-green">A</div>
            <div><div class="col-name">Akshay</div><div class="col-role">Azure Infrastructure</div></div>
            <span class="task-badge">3</span>
        </div>
        <div class="tasks">

            <div class="task-card">
                <div class="task-id">#AZ-001</div>
                <div class="task-title">Role assignment audit</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-done">Completed</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">20 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-low">Low</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">None</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-green"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-002</div>
                <div class="task-title">Service principal review</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-prog">In progress</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">28 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-med">Medium</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">Role audit</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-blue" style="width:60%"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-003</div>
                <div class="task-title">Subscription access report</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-delay">Delayed</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">25 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-high">High</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">SP review</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-red" style="width:30%"></div></div>
            </div>

        </div>
    </div>

    <!-- LENIN -->
    <div class="column col-lenin">
        <div class="col-header">
            <div class="avatar av-purple">L</div>
            <div><div class="col-name">Lenin</div><div class="col-role">DevOps & CI/CD</div></div>
            <span class="task-badge">3</span>
        </div>
        <div class="tasks">

            <div class="task-card">
                <div class="task-id">#AZ-004</div>
                <div class="task-title">DevOps pipeline setup</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-done">Completed</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">18 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-low">Low</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">None</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-green"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-005</div>
                <div class="task-title">Web app deployment</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-prog">In progress</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">30 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-med">Medium</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">Pipeline setup</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-blue" style="width:70%"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-006</div>
                <div class="task-title">Monitoring & alerts config</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-prog">In progress</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">05 Jul 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-low">Low</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">Web app deploy</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-blue" style="width:40%"></div></div>
            </div>

        </div>
    </div>

    <!-- SIVA -->
    <div class="column col-siva">
        <div class="col-header">
            <div class="avatar av-amber">S</div>
            <div><div class="col-name">Siva</div><div class="col-role">Security & Compliance</div></div>
            <span class="task-badge">3</span>
        </div>
        <div class="tasks">

            <div class="task-card">
                <div class="task-id">#AZ-007</div>
                <div class="task-title">IAM policy review</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-done">Completed</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">22 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-low">Low</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">None</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-green"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-008</div>
                <div class="task-title">Security compliance audit</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-prog">In progress</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">02 Jul 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-med">Medium</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">IAM policy review</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-blue" style="width:50%"></div></div>
            </div>

            <div class="task-card">
                <div class="task-id">#AZ-009</div>
                <div class="task-title">Access control documentation</div>
                <div class="task-fields">
                    <div class="field-row"><span class="field-key">Status</span><span class="badge b-delay">Delayed</span></div>
                    <div class="field-row"><span class="field-key">Due date</span><span class="date-val">24 Jun 2026</span></div>
                    <div class="field-row"><span class="field-key">Risk</span><span class="risk-high">High</span></div>
                    <div class="field-row"><span class="field-key">Dependency</span><span class="dep-val">Security audit</span></div>
                </div>
                <div class="progress"><div class="prog-fill p-red" style="width:20%"></div></div>
            </div>

        </div>
    </div>

</div>

<footer>
    Deployed via Azure DevOps &nbsp;|&nbsp; ERIKS IoT Project &nbsp;|&nbsp; Version 5.0 &nbsp;|&nbsp; Manager: Vivek R
</footer>

</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "5.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)