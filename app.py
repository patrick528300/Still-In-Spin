from flask import Flask, render_template, request, redirect
app = Flask(__name__)

id = 1

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addVehicle",methods=["GET"])
def addVehicle():
    return render_template("addVehicle.html")

@app.route("/vehicle",methods=["GET","POST"])
def handleVehicle():
    if request.method == "POST":
        year = request.form['year']
        make = request.form['make']
        model = request.form['model']
        color = request.form['color']
        init_mileage = request.form['mileage']
        id+=1
        print("Year: ", year)
        print("Make: ", make)
        print("Model: ", model)
        print("Color: ", color)
        print("initial mileage: ", init_mileage)
        return redirect("home.html",
                    id=id,year=year,model=model,
                    color=color,init_mileage=init_mileage)
    return render_template("addVehicle.html")


if __name__ == "__main__":
    app.run(debug=True)