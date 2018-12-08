from peewee import *
from employee import Employee
#when creating a database system, one should have the following 4 elemtns
try:
    db = PostgresqlDatabase("payrollsystem", user="postgres", password="0000", host="localhost")

except:
    print=("There is an error")

#We want to create the folloiwing tables: Employee that has a primary key; neme, KRA PIN, Department, position, basic_salary, house_allowance
#next we need to create another table called Payroll. it has the variable primary key, payroll key, overtime, hoouse allowance, others, NHIF, NSSF, PAYE
#IN THE SECOND TABLE WE NEED A FOREIGN KEY

class Payroll (Model):
    foreign_key=ForeignKeyField(Employee, backref='id', on)
    overtime=FloatField()
    basic_salary=FloatField()
    other_benefits=FloatField()
    house_allowance=FloatField()

    class Meta:
        database = db # This model uses the ".db" database.
        table_name = "payroll"


Payroll.create_table(fail_silently=True)

Class Compute_payroll(Payroll, Employee)
     
