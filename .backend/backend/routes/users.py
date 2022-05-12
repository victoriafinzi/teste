from flask import Flask

app = Flask(__name__)

@app.route('/')
def register_users():
    return '<h1> Olá </h1>'

app.run()