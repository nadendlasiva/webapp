from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #f0f0f0;">
            
            <h1 style="color: #0078d4;">🚀 Vivek</h1>

            <div style="margin-top: 20px;">
                <span style="background-color:#0078d4; color:white; padding:8px 14px; border-radius:20px; margin:5px; display:inline-block;">Akshay</span>
                <span style="background-color:#0078d4; color:white; padding:8px 14px; border-radius:20px; margin:5px; display:inline-block;">Lenin</span>
                <span style="background-color:#0078d4; color:white; padding:8px 14px; border-radius:20px; margin:5px; display:inline-block;">Siva</span>
            </div>

            <p style="color: #333; font-size: 18px; margin-top: 30px;">
                Version 2.0 - Successfully Deployed via Azure DevOps
            </p>

            <p style="color: green; font-size: 16px;">
                ✅ Pipeline is working correctly!
            </p>

            <hr style="width:50%; margin-top:30px;">

            <p style="color: #888;">
                Deployed by: nadendlasiva
            </p>

        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "2.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)