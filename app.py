from flask import Flask, render_template, request, redirect
app = Flask(__name__)

id = 1
vehicles = {}
class Vehicle:
    def __init__(self,id,year,make,model,color,mileage):
        self.id = id
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.init_mileage = mileage

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addVehicle",methods=["POST"])
def addVehicle():
    year = request.form['year']
    make = request.form['make']
    model = request.form['model']
    color = request.form['color']
    init_mileage = request.form['mileage']
    car = Vehicle(id,year,make,model,color,init_mileage)
    id+=1
    return redirect("home.html",
                    id=car.id,year=car.year,model=car.model,
                    color=car.color,init_mileage=car.init_mileage)


if __name__ == "__main__":
    app.run(debug=True)