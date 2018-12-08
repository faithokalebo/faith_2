from employee import Employee
from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route("/")#this creates route
def home():

    allEmployees = Employee.select()

    return render_template ("index.html", displayEmployees = allEmployees) #is only visible to index.html



@app.route("/employee")
def employeee():
    return render_template("add_employee.html")

@app.route("/saveEmployee", methods=["POST"])#
def saveEmp():
    name=request.form["form_full_name"]
    kra=request.form["form_kra_pin_number"]
    department=request.form["form_department"]
    position=request.form["form_position"]
    house_allowance=request.form["form_house_allowancce"]
    basic_salary=request.form["form_basic_salary"]

    Employee.create(full_name=name, kra_pin=kra,department=department,position=position, basic_salary=basic_salary, house_allowance=house_allowance)
    return redirect(url_for ("home"))

if __name__ == "__main__":
    app.run() #this creaates URL
    #after here were were todl to enter data inside the home function

