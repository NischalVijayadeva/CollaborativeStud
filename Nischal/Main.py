import unittest
from UnitTests import TestUT_Students as UT_Stud

if __name__ == "__main__":
    testStud = UT_Stud.TestUT_Students()
    
    # Setup test data for TC1
    # testStud.id = 2
    # testStud.name = "Test"
    # testStud.dept = "Bank"

    tc1 = unittest.FunctionTestCase(testStud.test_addStudent, setUp=testStud.setUp, tearDown=testStud.tearDown)

    # Setup test data for TC2
    tc2 = unittest.FunctionTestCase(testStud.test_getStudent, setUp=testStud.setUp, tearDown=testStud.tearDown)

    ts = unittest.TestSuite()
    ts.addTest(tc1)
    ts.addTest(tc2)

    runner = unittest.TextTestRunner()
    runner.run(ts)

   # unittest.main(verbosity=1)