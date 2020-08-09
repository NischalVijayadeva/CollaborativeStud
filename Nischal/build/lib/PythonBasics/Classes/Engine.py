from PythonBasics.Classes import Ignition
from PythonBasics.Enums import EngineConstants
    
class Engine:


    def __init__(self, engineType : EngineConstants.EngineType, fuelType: EngineConstants.FuelType):
        self.engineType = engineType
        self.fuelType = fuelType
        self.Valve = EngineConstants.EngineValve.VAL_TYPE
        self.ValveType = str(self.Valve.ValveType)
        self.Ignition = Ignition
        self.setIgnitionType()

    def setIgnitionType(self):
        if(self.engineType == EngineConstants.EngineType.ThermalEngine):
            if(self.fuelType == EngineConstants.FuelType.Petrol):
                self.Ignition = Ignition.IgnitionConstants.IgnitionType.DISTRIBUTOR_BASED
            else:
                self.Ignition = Ignition.IgnitionConstants.IgnitionType.DISTRIBUTOR_LESS
        else:
                self.Ignition = Ignition.IgnitionConstants.IgnitionType.COIL_ON_PLUG
