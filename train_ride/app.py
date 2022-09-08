from flask import Flask, render_template, request
from . import config
from . import db

app = Flask("train_ride")


@app.route("/")
def index():
    return render_template("index.html", config=config)

@app.route("/api/stations")
def stations():
    q = request.args.get("q")
    return db.search_stations(q)