

class Vehicle:
   
    charsis = True

    def __init__(self, wheels: int, gears: int):
        self.Wheels = wheels
        self.Gears = gears


class Car(Vehicle):

    def __init__(self, wheel, gear):
        super(Car,self).__init__(wheel, gear)
        self.speed = 0
        
class PremierPadmini(Car):        
    def __init__(self, wheel, gear):
        super(PremierPadmini,self).__init__(wheel, gear)
        self.doorType = "Inverted Type"

class Merc(Car):
    def __init__(self, wheel, gear):
        super(Merc, self).__init__(wheel, gear)
        self.color =  "red"


     

if __name__ == "__main__":
    
    premierPadmini = PremierPadmini(4,5)
    premierPadmini.charsis = False
    
    print("Type:",type(premierPadmini).__base__)

    print("Pemier Wheels = : ", premierPadmini.Wheels)
    print("Pemier Gears = : ",premierPadmini.Gears)
    print("Pemier Speed = : ", premierPadmini.speed)
    print("Pemier DoorType = : ", premierPadmini.doorType)
    print("Premier Charsis = : ", premierPadmini.charsis)


    merc = Merc(4,6)
    print("Merc Wheels = : ", merc.Wheels)
    print("Merc Gears = : ",merc.Gears)
    print("Mec Speed = : ", merc.speed)
    print("Merc color = :", merc.color)
    print("Merc Charsis = : ", merc.charsis)

    
  




    



    
    


