from enum import Enum

class ThermalEngineType(Enum):
    InternalCombustionEngine = "IC"
    ExternalCombustionEngine = "EC"

class ElectricalEngineType(Enum):
    ElectricMotor = "EM"

class EngineType(Enum):
    ThermalEngine = ThermalEngineType
    ElectricalEngine = ElectricalEngineType

class EngineValve(Enum):
    VAL_TYPE = EngineType


    def __init__(self,engineType: EngineType):
            self.engineType = engineType
    
    @property
    def ValveType(self):
        print("Valve Type:",self.value)

        if (self.value == EngineType.ThermalEngine):
            if (self.value == EngineType.ThermalEngine.value.InternalCombustionEngine):
                return 12
            else:
                return 16

class FuelType(Enum):
    Petrol = "Petrol"
    Desiel = "Desiel"
