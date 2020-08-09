from PythonBasics.Enums import EngineConstants

from enum import Enum, unique

class IgnitionType(Enum):
   DISTRIBUTOR_BASED = 0
   DISTRIBUTOR_LESS = 1
   COIL_ON_PLUG = 2

# class Ignition(Enum):
#     MANUAL_THERMAL = (EngineConstants.EngineType.ThermalEngine, IgnitionType.Manual)
#     MANUAL_ELECTRIC = (EngineConstants.EngineType.ElectricalEngine, IgnitionType.Manual)
#     SELF_ELECTRIC = (EngineConstants.EngineType.ElectricalEngine, IgnitionType.Self)
#     SELF_THERMAL = (EngineConstants.EngineType.ThermalEngine, IgnitionType.Self)

#     def __init__(self, engineType: EngineConstants.EngineType, ignitionType: IgnitionType):
#         self.engineType = engineType
#         self.ignitionType = ignitionType
       

#     @property
#     def FuelType(self):
#         print("Type:",self)

#         if (self.engineType == EngineConstants.EngineType.ThermalEngine):
#             if (self.ignitionType == IgnitionType.Self):
#                 return EngineConstants.FuelType.Petrol
#             else:
#                 return EngineConstants.FuelType.Desiel
#         else:
#             return "Electic"
        