from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "OOh Boy this is Docker"