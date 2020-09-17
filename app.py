from flask import Flask
from datetime import datetime
app=Flask(__name__)
@app.route("/")
def new():
    return "hello this is /"
@app.route("/new")
def indext():
    return "hello this is /new"
@app.route("/dhanraj")
def pp():
    return "hello this is /dhanraj"
