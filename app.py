from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: #f0f0f0;">
            <h1 style="color: #0078d4;">🚀 Hello from Python Web App on Azure! Siva Nadendla</h1>
            <p style="color: #333; font-size: 18px;">Version 2.0 - Successfully Deployed via Azure DevOps</p>
            <p style="color: green; font-size: 16px;">✅ Pipeline is working correctly!</p>
            <hr>
            <p style="color: #888;">Deployed by: nadendlasiva</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "2.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)