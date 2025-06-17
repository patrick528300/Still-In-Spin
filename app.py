from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("vehicle.html")

@app.route("/add",methods=["POST"])
def add_record():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)