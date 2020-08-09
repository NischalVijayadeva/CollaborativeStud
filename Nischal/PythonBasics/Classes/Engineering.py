from enum import Enum

class DepartmentType(Enum):
    COMPUTER_SCIENCE = 0
    ELECTRONICS = 1
    MECHANICAL = 2



class Department:
    def __init__(self):
        self.Name = ""
        self.hod =""
        self.college = ""
        self.courses = list()
        self.type = None
        

    def getAllCourse(self):
        print("Displaying all courses of department : ",self.Name)
        for index in range(len(self.courses)):
            print(self.courses[index])
    
    def getDeparmentType(self):
         print("Department type : ",self.type.name)

    def addCourse(self, courseName):
        self.courses.append(courseName)

class Computers(Department):
    def __init__(self):
        super(Computers,self).__init__()
        self.type = DepartmentType.COMPUTER_SCIENCE

    
class Electronics(Department):
    def __init__(self):
        super(Electronics,self).__init__()
        self.type = DepartmentType.ELECTRONICS

    
if __name__ == "__main__":

    electronicDep = Electronics()
    electronicDep.Name = "Electronics"
    electronicDep.hod = "Sharan"
    electronicDep.college = "Bhasaveshawara Engineering College"

    electronicDep.addCourse("VLSI")
    electronicDep.addCourse("Em sys")

    electronicDep.getAllCourse()
    electronicDep.getDeparmentType()

    csDep = Computers()
    csDep.Name = "Computer"
    csDep.hod = "Deepak"
    csDep.college = "MVJIT"

    csDep.addCourse("C++")
    csDep.addCourse("Java")

    csDep.getAllCourse()
    csDep.getDeparmentType()
