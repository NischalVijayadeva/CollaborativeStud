import PythonBasics
from enum import Enum, unique
from abc import ABC, ABCMeta, abstractmethod

from PythonBasics.Classes import Engine 
from PythonBasics.Enums import IgnitionConstants, VehicleConstants



class Vehicle:

    def __init__(self, 
    bodyType: VehicleConstants.BodyType,
    vehicleType: VehicleConstants.VehicleType,
    engineType: Engine.EngineConstants.EngineType,
    fuelType: Engine.EngineConstants.FuelType ):
        self.Wheels = 1
        self.Gear = 1
        self.BodyType = VehicleConstants.BodyType.Nothing
        self.VehicleType = vehicleType
        self.EngineType = engineType
        self.FuelType = fuelType
       
        self.Engine = Engine.Engine(engineType,fuelType)
        
        print("Factory Setting for Power : {} HP".format(self.Engine.power))



        if (isinstance (bodyType,VehicleConstants.BodyType)):
            self.bodyType = bodyType

        if (isinstance(vehicleType, VehicleConstants.VehicleType)):
            self.vehicleType = vehicleType

   # @abstractmethod
    def startEngine(self):
        self.Engine.crankIgnition()
        print("{} has started".format(self.VehicleType.name))


# if __name__ == "__main__":



#     vehicle = Vehicle(BodyType.Fiber,
#     VehicleType.Nothing,
#     Engine.EngineConstants.EngineType.ThermalEngine,
#     Engine.EngineConstants.FuelType.Petrol)
    
       
#     vehicle.Wheels = 4
#     print(vehicle.Engine.FuelType)