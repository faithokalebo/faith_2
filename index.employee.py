from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")#this creates route
def employee():

    return render_template ("add_employee.html") #is only visible to index.html


if __name__ == "__main__":
    app.run(debug=True, port='5005') #this creaates URL
    #after here were were told to enter data inside the home function

