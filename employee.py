from peewee import *
#when creating a database system, one should have the following 4 elemtns
try:
    db = PostgresqlDatabase("dpapl6kbou6m8", user="aukjdazlpivyvs", password="eca710ddc82f34f00dfa674b82e9f39381298a006647c1a282321ce657e34d28", host="ec2-54-235-133-42.compute-1.amazonaws.com")

except:
    print=("There is an error")

#We want to create the folloiwing tables: Employee that has a primary key; neme, KRA PIN, Department, position, basic_salary, house_allowance
#next we need to create another table called Payroll. it has the variable primary key, payroll key, overtime, hoouse allowance, others, NHIF, NSSF, PAYE
#IN THE SECOND TABLE WE NEED A FOREIGN KEY


class Employee (Model):
    full_name = CharField('100')
    kra_pin=CharField()
    department=CharField()
    position=CharField()
    basic_salary=FloatField()
    house_allowance=FloatField()
    print("Sucessfully connected")

    class Meta:
        database = db # This model uses the ".db" database.
        table_name = "employee2"


Employee.create_table(fail_silently=True)
x=2

