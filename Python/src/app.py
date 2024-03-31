# Index File implemented
from flask import flask
app = flask(__name__)
@app.route("/")
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
