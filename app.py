from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to My Flask App</h1>
    <p>Try visiting <a href="/hello/World">/hello/World</a></p>
    '''

@app.route('/hello/<name>')
def hello(name):
    return f'<h2>Hello, {name}!</h2>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
