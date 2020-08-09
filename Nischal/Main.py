import unittest

from PythonBasics.Classes import Vehicle
from PythonBasics.Enums.EngineConstants import EngineType, FuelType
from PythonBasics.Enums.VehicleConstants import BodyType, VehicleType

from UnitTests import TestUT_Students as UT_Stud


# class Car(IVehicle.IVehicle):
#     def __init__(self):
#         super(IVehicle.IVehicle,self).__init__()
#         self.__
#         veh = IVehicle.IVehicle(
#             BodyType.Fiber,
#             VehicleType.Nothing,
#             EngineType.TWO_STOKE,
#             FuelType.Petrol
#          )

#     def startEngine(self):
#         print("start")

if __name__ == "__main__":
    # testStud = UT_Stud.TestUT_Students()
    
    # Setup test data for TC1
    # testStud.id = 2
    # testStud.name = "Test"
    # testStud.dept = "Bank"

    # tc1 = unittest.FunctionTestCase(testStud.test_addStudent, setUp=testStud.setUp, tearDown=testStud.tearDown)

    # # Setup test data for TC2
    # tc2 = unittest.FunctionTestCase(testStud.test_getStudent, setUp=testStud.setUp, tearDown=testStud.tearDown)

    # ts = unittest.TestSuite()
    # ts.addTest(tc1)
    # ts.addTest(tc2)

    # runner = unittest.TextTestRunner()
    # runner.run(ts)

    #--------------------------
    #  Vehicle invocation
    #--------------------------


    # vehicle = Vehicle.Vehicle(
    #     Vehicle.BodyType.Fiber,
    #     Vehicle.VehicleType.Nothing,
    #     Vehicle.Engine.EngineConstants.EngineType.TWO_STOKE,
    #     Vehicle.Engine.EngineConstants.FuelType.Petrol
    # )


    # vehicle = IVehicle.Vehicle(
    #     BodyType.Fiber,
    #     VehicleType.Nothing,
    #     EngineType.TWO_STOKE,
    #     FuelType.Petrol
    # )

    # veh = IVehicle.Vehicle(
    #     IVehicle.Vehicle..BodyType.Fiber,
    #     IVehicle.Vehicle.VehicleType.Nothing,
    #     IVehicle.Vehicle.Engine.EngineConstants.EngineType.TWO_STOKE,
    #     IVehicle.Vehicle.Engine.EngineConstants.FuelType.Petrol
    # )

    
    
    
    vehicle = Vehicle.Vehicle(
        BodyType.Fiber,
        VehicleType.Car,
        EngineType.TWO_STOKE,
        FuelType.Petrol
    )
    vehicle.Engine.rpm = 3400
    vehicle.Engine.overallVehicleWeight = 1000
    vehicle.Engine.recaliburateEngine()
       
    vehicle.Wheels = 4
    print(vehicle.Engine.fuelType)
    print("Power retuned to -- : {} HP".format(vehicle.Engine.power))

    vehicle.startEngine()

   # unittest.main(verbosity=1)
