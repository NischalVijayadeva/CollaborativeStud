from enum import Enum

class ThermalEngine(Enum):
    InternalCombustionEngine = "IC"
    ExternalCombustionEngine = "EC"
    ReactionEngine = "RE"

class ElectricalEngine(Enum):
    ElectricMotor = "EM"

class EngineCategory(Enum):
    ThermalEngine = ThermalEngine
    ElectricalEngine = ElectricalEngine

class EngineType(Enum):
    TWO_STOKE = 2
    FOUR_STOKE = 4

class EngineValve(Enum):
    VAL_TYPE = EngineCategory


    def __init__(self,engineType: EngineCategory):
            self.engineType = engineType
    
    @property
    def ValveType(self):
        print("Valve Type:",self.value)

        if (self.value == EngineCategory.ThermalEngine):
            if (self.value == EngineCategory.ThermalEngine.value.InternalCombustionEngine):
                return 12
            else:
                return 16

class FuelType(Enum):
    Petrol = "Petrol"
    Desiel = "Desiel"
