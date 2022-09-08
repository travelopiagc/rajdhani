from flask import Flask, render_template
from . import config

app = Flask("train_ride")


@app.route("/")
def index():
    return render_template("index.html", config=config)
