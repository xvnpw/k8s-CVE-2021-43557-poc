from flask import Flask

app = Flask(__name__)

@app.route('/public')
def public():
    return {
        "data": "public data",
    }
