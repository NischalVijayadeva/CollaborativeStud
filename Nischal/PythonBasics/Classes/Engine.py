from PythonBasics.Classes import Ignition
from PythonBasics.Enums import EngineConstants
import math
    
class Engine:

    class SparkPlugs():

        def __init__(self, ignitionType):
            self.sparkPlugType = self.getSparkPlugType(ignitionType)
            self.numberOfSparkPlugs = 0


        def getSparkPlugType(self,ignitionType:Ignition.IgnitionConstants.IgnitionType):
            
             switcher = {
                 
                Ignition.IgnitionConstants.IgnitionType.HIGH_ENERGY:
                    Ignition.IgnitionConstants.SparkPlugType.DOUBLE_PLATINUM_SPARK_PLUG,
                
                Ignition.IgnitionConstants.IgnitionType.COIL_ON_PLUG:
                    Ignition.IgnitionConstants.SparkPlugType.SINGLE_PLATINUM_SPARK_PLUG,

                Ignition.IgnitionConstants.IgnitionType.DISTRIBUTOR_LESS:
                    Ignition.IgnitionConstants.SparkPlugType.SILVER_SPARK_PLUG
             }
             return switcher.get(ignitionType)



    def __init__(self, engineType : EngineConstants.EngineType, fuelType: EngineConstants.FuelType):
        self.engineType = engineType
        self.fuelType = fuelType
        self.Valve = EngineConstants.EngineValve.VAL_TYPE
        self.ValveType = str(self.Valve.ValveType)
        self.ignitionType = self.getIgnitionType()
        self.Ignition = Ignition.Ignition(self.ignitionType)
        self.overallVehicleWeight = 100
        self.rpm = 2000
        self.power = 0
        self.torque = 0
        self.setEngineParameters(self.ignitionType)

    def getIgnitionType(self):
        if(self.engineType == EngineConstants.EngineType):
            if(self.fuelType == EngineConstants.FuelType.Petrol):
                return Ignition.IgnitionConstants.IgnitionType.HIGH_ENERGY
            else:
                return  Ignition.IgnitionConstants.IgnitionType.DISTRIBUTOR_LESS
        else:
                return  Ignition.IgnitionConstants.IgnitionType.COIL_ON_PLUG
    
    def getNumberOfSparkPlugs(self,engineType:EngineConstants.EngineType):
        switcher={
            engineType.TWO_STOKE: 1,
            engineType.FOUR_STOKE: 2
        }
        return switcher.get(engineType)

    def calculatePowerByWeight(self, weight, rpm):
        radius = 1 # 1 ft 
        distancePerRevolution = 2 * math.pi * radius
        
        distancePerMin = distancePerRevolution * rpm
        # power = force * distance / time (in Min)
        # power calculated @ ft-lb per min
        power = weight * distancePerMin 

        # power in HP
        # By definition HP = 33000 foot-pound of work per min
        return (power / 33000)

    def setEngineParameters(self, ignitionType:Ignition.IgnitionConstants.IgnitionType):
        self.sparkPlugs = self.SparkPlugs(ignitionType)
        self.sparkPlugs.numberOfSparkPlugs = self.getNumberOfSparkPlugs(self.engineType)
        self.power =   (self.calculatePowerByWeight(self.overallVehicleWeight,self.rpm)).__round__(1)
        self.torque = (self.power * 5252) / self.rpm

    def recaliburateEngine(self):
        self.setEngineParameters(self.ignitionType)

    def crankIgnition(self):
        self.Ignition.crank()

