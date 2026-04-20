from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Azure Web App!</h1>'

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run()
