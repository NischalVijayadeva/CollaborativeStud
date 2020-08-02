
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employees:

   
    def __init__(self):
        self.employees = list()

    def addNewEmployee(self, employee):
        self.employees.append(employee)
     
    def getEmployeeByName(self, name):
        for e in self.employees:
            if (e.name == name):
                return e

    def removeEmployee(self, name):
         emp = self.getEmployeeByName(name)
         if (emp is not None):
            self.employees.remove(emp)
