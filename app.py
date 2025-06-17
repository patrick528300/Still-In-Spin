from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add_record():
    return redirect("/")