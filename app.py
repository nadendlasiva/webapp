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
    <title>Azure DevOps Migration Runbook</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8f9fa; min-height: 100vh; }
        .top-bar { background: #0078d4; color: white; padding: 10px 24px; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 10px; }
        .monitors { display: flex; gap: 10px; padding: 12px 24px; background: #f0f6ff; border-bottom: 1px solid #d0e4f7; flex-wrap: wrap; align-items: center; }
        .monitor-chip { display: flex; align-items: center; gap: 8px; background: white; border: 1px solid #d0e4f7; border-radius: 20px; padding: 6px 14px; }
        .av { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; flex-shrink: 0; }
        .av-blue   { background: #cce4f7; color: #004f8c; }
        .av-green  { background: #c0dd97; color: #27500a; }
        .av-purple { background: #cecbf6; color: #26215c; }
        .av-amber  { background: #fac775; color: #412402; }
        .chip-name { font-size: 12px; font-weight: 600; color: #1a1a1a; }
        .chip-role { font-size: 10px; color: #666; }
        .monitor-label { font-size: 11px; color: #0078d4; font-weight: 600; margin-left: auto; }
        .stats-bar { display: flex; gap: 12px; padding: 14px 24px; background: white; border-bottom: 1px solid #e0e0e0; flex-wrap: wrap; }
        .stat { background: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 8px; padding: 8px 20px; text-align: center; min-width: 90px; }
        .stat-num { font-size: 22px; font-weight: 600; }
        .stat-lbl { font-size: 11px; color: #666; margin-top: 2px; }
        .s-blue  { color: #0078d4; }
        .s-green { color: #107c10; }
        .s-amber { color: #835b00; }
        .s-red   { color: #c50f1f; }
        .content { padding: 20px 24px; }
        .section-card { background: white; border: 1px solid #e0e0e0; border-radius: 10px; margin-bottom: 20px; overflow: hidden; }
        .section-header { padding: 14px 18px; background: #f0f6ff; border-bottom: 1px solid #d0e4f7; display: flex; align-items: center; gap: 10px; }
        .section-header h2 { font-size: 14px; font-weight: 600; color: #004f8c; }
        .section-header span { font-size: 11px; color: #666; margin-left: auto; }
        .board { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; padding: 16px; }
        .col-header { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 8px; margin-bottom: 10px; }
        .col-header-l { background: #EEEDFE; border-top: 3px solid #534AB7; border-radius: 0 0 8px 8px; }
        .col-header-s { background: #FAEEDA; border-top: 3px solid #854F0B; border-radius: 0 0 8px 8px; }
        .col-name-l { font-size: 13px; font-weight: 600; color: #26215c; }
        .col-name-s { font-size: 13px; font-weight: 600; color: #412402; }
        .col-role { font-size: 10px; color: #666; margin-top: 1px; }
        .cnt { margin-left: auto; font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 20px; }
        .cnt-l { background: #CECBF6; color: #26215c; }
        .cnt-s { background: #FAC775; color: #412402; }
        .task { background: #fafafa; border: 1px solid #e8e8e8; border-radius: 6px; padding: 11px; margin-bottom: 8px; transition: box-shadow 0.2s; }
        .task:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.08); background: white; }
        .task:last-child { margin-bottom: 0; }
        .tid { font-size: 10px; color: #0078d4; font-weight: 600; margin-bottom: 3px; }
        .ttitle { font-size: 12px; font-weight: 600; color: #1a1a1a; margin-bottom: 8px; line-height: 1.4; }
        .tfields { border-top: 1px solid #f0f0f0; padding-top: 7px; display: flex; flex-direction: column; gap: 4px; }
        .trow { display: flex; justify-content: space-between; align-items: center; }
        .tkey { font-size: 10px; color: #666; }
        .badge { font-size: 9px; font-weight: 600; padding: 2px 8px; border-radius: 20px; }
        .b-done { background: #dff6dd; color: #107c10; }
        .b-prog { background: #cce4f7; color: #004f8c; }
        .b-pend { background: #fff4ce; color: #835b00; }
        .risk-l { font-size: 9px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #dff6dd; color: #107c10; }
        .risk-m { font-size: 9px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #fff4ce; color: #835b00; }
        .risk-h { font-size: 9px; font-weight: 600; padding: 2px 8px; border-radius: 20px; background: #fde7e9; color: #c50f1f; }
        .dval { font-size: 9px; color: #666; font-style: italic; }
        .prog { height: 3px; background: #e0e0e0; border-radius: 2px; margin-top: 7px; }
        .pf { height: 100%; border-radius: 2px; }
        .pf-g { background: #107c10; width: 100%; }
        .pf-b { background: #0078d4; }
        .pf-p { background: #5c2d91; }
        .pf-a { background: #835b00; }
        footer { text-align: center; padding: 16px; color: #888; font-size: 11px; border-top: 1px solid #e0e0e0; background: white; margin-top: 8px; }
    </style>
</head>
<body>

<div class="top-bar">&#9651; Azure DevOps Migration Runbook &nbsp;|&nbsp; Classic Pipeline Migration</div>

<div class="monitors">
    <div class="monitor-chip">
        <div class="av av-blue">VR</div>
        <div><div class="chip-name">Vivek R</div><div class="chip-role">Project Manager</div></div>
    </div>
    <div class="monitor-chip">
        <div class="av av-green">AK</div>
        <div><div class="chip-name">Akshay</div><div class="chip-role">Tech Lead</div></div>
    </div>
    <div class="monitor-label">&#128065; Monitoring all tasks</div>
</div>

<div class="stats-bar">
    <div class="stat"><div class="stat-num s-blue">18</div><div class="stat-lbl">Total tasks</div></div>
    <div class="stat"><div class="stat-num s-green">4</div><div class="stat-lbl">Completed</div></div>
    <div class="stat"><div class="stat-num s-amber">10</div><div class="stat-lbl">In progress</div></div>
    <div class="stat"><div class="stat-num s-red">4</div><div class="stat-lbl">Pending</div></div>
</div>

<div class="content">

    <div class="section-card">
        <div class="section-header">
            <h2>&#127970; Runbook 1 &mdash; Full organization migration (tenant to tenant)</h2>
            <span>9 tasks</span>
        </div>
        <div class="board">
            <div>
                <div class="col-header col-header-l">
                    <div class="av av-purple">L</div>
                    <div><div class="col-name-l">Lenin</div><div class="col-role">DevOps Engineer</div></div>
                    <span class="cnt cnt-l">5</span>
                </div>
                <div class="task">
                    <div class="tid">#ORG-001</div>
                    <div class="ttitle">Inventory all projects, repos & pipelines in source org</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-done">Completed</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">None</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-g"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-002</div>
                    <div class="ttitle">Create new Azure DevOps org in target tenant</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-done">Completed</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-001</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-g"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-003</div>
                    <div class="ttitle">Migrate all Git repositories to target org</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-002</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-b" style="width:70%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-004</div>
                    <div class="ttitle">Export & recreate classic pipelines in target org</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-h">High</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-003</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-b" style="width:40%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-005</div>
                    <div class="ttitle">Validate & run all pipelines end-to-end in target</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-pend">Pending</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-h">High</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-004</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-a" style="width:10%"></div></div>
                </div>
            </div>
            <div>
                <div class="col-header col-header-s">
                    <div class="av av-amber">S</div>
                    <div><div class="col-name-s">Siva</div><div class="col-role">Cloud Engineer</div></div>
                    <span class="cnt cnt-s">4</span>
                </div>
                <div class="task">
                    <div class="tid">#ORG-006</div>
                    <div class="ttitle">Migrate service connections & variable groups</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-002</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-b" style="width:50%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-007</div>
                    <div class="ttitle">Reassign users & permissions in target org</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-006</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-b" style="width:40%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-008</div>
                    <div class="ttitle">Migrate agent pools & self-hosted agents</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-pend">Pending</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-007</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-a" style="width:15%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#ORG-009</div>
                    <div class="ttitle">Decommission source org after cutover sign-off</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-pend">Pending</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-h">High</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">ORG-005</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-a" style="width:5%"></div></div>
                </div>
            </div>
        </div>
    </div>

    <div class="section-card">
        <div class="section-header">
            <h2>&#128193; Runbook 2 &mdash; Single project migration (org to org)</h2>
            <span>9 tasks</span>
        </div>
        <div class="board">
            <div>
                <div class="col-header col-header-l">
                    <div class="av av-purple">L</div>
                    <div><div class="col-name-l">Lenin</div><div class="col-role">DevOps Engineer</div></div>
                    <span class="cnt cnt-l">5</span>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-001</div>
                    <div class="ttitle">Export project data — repos, boards, pipelines</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-done">Completed</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">None</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-g"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-002</div>
                    <div class="ttitle">Create target project in destination org</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-done">Completed</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-001</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-g"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-003</div>
                    <div class="ttitle">Migrate repos & branch policies to target project</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-002</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-p" style="width:60%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-004</div>
                    <div class="ttitle">Recreate classic build & release pipelines</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-h">High</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-003</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-p" style="width:35%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-005</div>
                    <div class="ttitle">Test all pipelines & validate deployment gates</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-pend">Pending</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-h">High</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-004</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-a" style="width:5%"></div></div>
                </div>
            </div>
            <div>
                <div class="col-header col-header-s">
                    <div class="av av-amber">S</div>
                    <div><div class="col-name-s">Siva</div><div class="col-role">Cloud Engineer</div></div>
                    <span class="cnt cnt-s">4</span>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-006</div>
                    <div class="ttitle">Migrate work items & backlogs to target project</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-002</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-p" style="width:55%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-007</div>
                    <div class="ttitle">Recreate service connections & environments</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-002</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-p" style="width:45%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-008</div>
                    <div class="ttitle">Add team members & set permissions in target</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-prog">In progress</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-l">Low</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-007</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-p" style="width:30%"></div></div>
                </div>
                <div class="task">
                    <div class="tid">#PRJ-009</div>
                    <div class="ttitle">Archive source project & notify stakeholders</div>
                    <div class="tfields">
                        <div class="trow"><span class="tkey">Status</span><span class="badge b-pend">Pending</span></div>
                        <div class="trow"><span class="tkey">Risk</span><span class="risk-m">Medium</span></div>
                        <div class="trow"><span class="tkey">Dependency</span><span class="dval">PRJ-005</span></div>
                    </div>
                    <div class="prog"><div class="pf pf-a" style="width:5%"></div></div>
                </div>
            </div>
        </div>
    </div>

</div>

<footer>
    Deployed via Azure DevOps &nbsp;|&nbsp; Migration Runbook &nbsp;|&nbsp; Version 6.0 &nbsp;|&nbsp; Monitor: Vivek R &amp; Akshay
</footer>

</body>
</html>
"""

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "6.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)