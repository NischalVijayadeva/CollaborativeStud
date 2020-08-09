from PythonBasics.Enums import IgnitionConstants

class Ignition:
    
     
    def __init__(self, ignitionType: IgnitionConstants.IgnitionType):
        self.IgnitionType = ignitionType

    def crank(self):
        print("Sparking with Ignition Type : {}".format(self.IgnitionType))
    

    

  
