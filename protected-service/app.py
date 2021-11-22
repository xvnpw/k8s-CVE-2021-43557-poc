from flask import Flask

app = Flask(__name__)

@app.route('/protected')
def public():
    return {
        "data": "protected data",
    }
