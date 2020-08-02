import unittest 

import Models.Student as stud

students = list()

class Students:
  def __init__(self):
      self.students = students

  def addStudent(self, name, dept):
     id = len(self.students) + 1
     self.students.append(stud.Student(id, name, dept))
     return id

  def removeStudentById(self, id):
     stud = self.getStudentById(id)
     self.students.remove(stud)
     

  def getStudentById(self, id):
      print("Total Studnts : {} ".format(len(self.students)))
      for s in self.students:
        if (s.id == id):
           print (s.id)
           return s

  
