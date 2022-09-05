from flask import Flask, render_template


app = Flask("train_ride")


@app.route("/")
def index():
    return render_template("hello.html")
