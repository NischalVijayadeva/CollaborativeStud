class Human:
    
    SPECIES = "HOMOSPAPIENT"

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.height=0
        
    def walk(self):
        walking = "Yes"
        print("{} is Walking!!".format(self.name))

    def talk(self):
        talking = "Yes"
        print("{} is talking".format(self.name))

# if __name__ == "__main__":
#     human = Human("Nischal","Male")
#     human.walk()
#     human.talk()


    
class Boy(Human):

    def __init__(self, name, *args,**kwargs):
        super(Boy,self).__init__(name,"Male",*args,**kwargs)
        self.name = name

class Girl(Human):

    def __init__(self, name, *args,**kwargs):
        super(Girl,self).__init__(name,"Female",*args,**kwargs)
        self.name = name
        self.age = 0



if __name__ == "__main__":
    boy = Boy("Sharan")
    boy.walk()
    boy.talk()
    boy.height=174
   

    print(boy.SPECIES)

    boy.SPECIES = "XYZ"

    print(boy.SPECIES)


    girl = Girl("Priya")
    girl.walk()
    girl.talk()
    girl.age=10
    girl.height=200




    print(girl.SPECIES)

    girl.SPECIES = "ABC"

    print(girl.SPECIES)


    print("Gender of the boy : {}".format(boy.gender))

