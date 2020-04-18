class PartyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print("Contructor Initialized")
    def party(self):
        self.x=self.x+1
        print(self.name," has partied ", self.x,"times")
    # def __del__(self):
    #     print("Constructor Destructed",self.x)

class Football(PartyAnimal): #Football Extends Party Animal
    points=0
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print(self.name,"points",self.points)
    
obj1=PartyAnimal("Arnab")
obj1.party()
obj1.party()

obj2=Football("Ronnie")
obj2.touchdown()

