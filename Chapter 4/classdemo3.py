class PartyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print("Contructor Initialized")
    def party(self):
        self.x=self.x+1
        print(self.name," has partied ", self.x,"times")
    def __del__(self):
        print("Constructor Destructed",self.x)

obj1=PartyAnimal("Arnab")
obj1.party()
obj1.party()

obj2=PartyAnimal("Ronnie")
obj2.party()

obj1.party()
