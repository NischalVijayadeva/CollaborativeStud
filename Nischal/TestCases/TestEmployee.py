import unittest
from TestCases import EmployeeClass as Emp
# class Employee:
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age


class TestEmployeeSuite(unittest.TestCase):
    
    def __init__(self,*args,**kwargs):
        super(TestEmployeeSuite,self).__init__(*args, **kwargs)
        self.employees = Emp.Employees()
        self.employeelist = self.employees.employees
        #list()

    def classSetup(self):
        e = Emp.Employee("t1",1)
        
        self.employees.addNewEmployee(e)
        #self.addEmployee("t2",2) 

    def addEmployee(self,name, age):
        self.employees.addNewEmployee(Emp.Employee(name,age))

    def getEmployee(self, name):
        for e in self.employeelist:
          if (e.name == name):
              return e
        
    def test_AddEmployee(self):
        name = "t1"
        employee = self.getEmployee(name)

        if (len(self.employeelist) > 0): 
            self.assertIn(employee, self.employeelist, "Employee {} does not exist".format(name))
           

if __name__ == "__main__":
    # employeeTc = TestEmployeeSuite()

    # ftc1 = unittest.FunctionTestCase(employeeTc.TestAddEmployee,
    # setUp=employeeTc.classSetup)

    # ts = unittest.TestSuite()
    # ts.addTest(ftc1)
        
    # runner = unittest.TextTestRunner()
    # runner.run(ts)
    
    unittest.main()