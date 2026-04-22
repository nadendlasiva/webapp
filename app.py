from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #e6f2fb, #f9fcff);
                text-align: center;
                margin-top: 40px;
            }

            h1 {
                color: #0078d4;
            }

            .org {
                margin: 20px 0;
                font-size: 20px;
                font-weight: bold;
            }

            .flow-container {
                width: 80%;
                margin: 40px auto;
                position: relative;
                height: 120px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 6px 15px rgba(0,0,0,0.15);
                overflow: hidden;
            }

            .resource {
                position: absolute;
                top: 40px;
                font-size: 32px;
                animation: move 6s linear infinite;
            }

            .storage { animation-delay: 0s; }
            .app { animation-delay: 1.5s; }
            .monitor { animation-delay: 3s; }
            .devops { animation-delay: 4.5s; }

            @keyframes move {
                0% { left: -50px; opacity: 0; }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { left: 100%; opacity: 0; }
            }

            table {
                margin: 40px auto;
                width: 80%;
                border-collapse: collapse;
                background: white;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }

            th {
                background: #0078d4;
                color: white;
                padding: 12px;
            }

            td {
                padding: 12px;
                border-bottom: 1px solid #ddd;
            }

            footer {
                margin-top: 30px;
                color: #666;
            }
        </style>
    </head>

    <body>

        <h1>☁️ Azure Live Resource Activity</h1>

        <div class="org">👑 Vivek → Assigning work to Azure Resources</div>

        <!-- LIVE MOTION FLOW -->
        <div class="flow-container">
            <div class="resource storage">🗄️</div>
            <div class="resource app">🌐</div>
            <div class="resource monitor">📊</div>
            <div class="resource devops">⚙️</div>
        </div>

        <table>
            <tr>
                <th>Role</th>
                <th>Name</th>
                <th>Responsibility</th>
                <th>Platform</th>
            </tr>
            <tr>
                <td>Team Lead</td>
                <td>Vivek</td>
                <td>Work Assignment</td>
                <td>Azure</td>
            </tr>
            <tr>
                <td>Team Member</td>
                <td>Akshay</td>
                <td>Full Access – Admin</td>
                <td>Azure</td>
            </tr>
            <tr>
                <td>Team Member</td>
                <td>Lenin</td>
                <td>Full Access – Admin</td>
                <td>Azure</td>
            </tr>
            <tr>
                <td>Team Member</td>
                <td>Siva</td>
                <td>Limited Access</td>
                <td>Azure DevOps</td>
            </tr>
        </table>

        <p style="color: green; font-weight: bold;">
            ✅ Live Azure resource activity simulation
        </p>

        <footer>
            Deployed via Azure DevOps | Version 3.0
        </footer>

    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "animation": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)