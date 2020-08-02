import unittest
from Models import Students as stud
import Models.Student as st


class TestUT_Students(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(TestUT_Students,self).__init__(*args,**kwargs)
    self.students = stud.Students()

  def setUp(self):
    self.students = stud.Students()

    self.id = 1
    self.name = "Nischal"
    self.dept = "IT"

  def tearDown(self):
    self.students = None

  def studentTeardown(self):
    self.students = None

  
  def test_getStudent(self):
    print ("\nFetch student id {} ".format(self.id))
    print ("\nCount of Students internally : {}".format(len(self.students.students)))
    std1 = self.students.getStudentById(self.id)
    std1.__class__ = st.Student
    self.assertIn(std1, self.students.students, "Student with ID: {} does not exist".format(std1.name))

  def test_addStudent(self):
    print("In Add Student Method")
    print("-----------------------------")
    id = self.students.addStudent(self.name, self.dept)
    stud1 = self.students.getStudentById(id)
    self.assertIn(stud1, self.students.students, "Student {} does not exist".format(stud1.name))
    print("\nExiting Add Student Method")
    print("-----------------------------")


if __name__ == "__main__":
  unittest.main()