from enum import Enum, unique

@unique
class BodyType(Enum):
    Nothing=0
    Metal = 1
    Fiber = 2
    Hybrid = 3

@unique
class VehicleType(Enum):
    Nothing=0
    Cycle = 1
    Car = 2
    Bus = 3
    Truck = 4