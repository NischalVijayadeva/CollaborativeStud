
from enum import Enum, unique

from PythonBasics.Classes import Engine 
from PythonBasics.Enums import IgnitionConstants


@unique
class BodyType(Enum):
    Nothing=0
    Metal = 1
    Fiber = 2
    Hybrid = 3

@unique
class VehicleType(Enum):
    Nothing=0
    Cycle:1
    Car:2
    Bus:3
    Truck:4




class Vehicle:

   def __init__(self, 
   bodyType: BodyType,
   vehicleType: VehicleType,
   engineType: Engine.EngineConstants.EngineType,
   fuelType: Engine.EngineConstants.FuelType ):
        self.Wheels = 1
        self.Gear = 1
        self.BodyType = BodyType.Nothing
        self.VehicleType = VehicleType.Nothing
        self.EngineType = engineType
        self.FuelType = fuelType

        self.Engine = Engine.Engine(engineType,fuelType)

        print("Types -- : ", self.Engine.ValveType)



        if (isinstance (bodyType,BodyType)):
            self.bodyType = bodyType

        if (isinstance(vehicleType, VehicleType)):
            self.vehicleType = vehicleType



# if __name__ == "__main__":



#     vehicle = Vehicle(BodyType.Fiber,
#     VehicleType.Nothing,
#     Engine.EngineConstants.EngineType.ThermalEngine,
#     Engine.EngineConstants.FuelType.Petrol)
    
       
#     vehicle.Wheels = 4
#     print(vehicle.Engine.FuelType)