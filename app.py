from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Render!</h1><p>This is a pure Python web app hosted online.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
  
