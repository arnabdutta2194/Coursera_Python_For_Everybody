class PartyAnimal:
    x=0
    def __init__(self):
        print("Contructor Initialized")
    def party(self):
        self.x=self.x+1
        print("Current number: ", self.x)
    def __del__(self):
        print("Constructor Destructed",self.x)

obj=PartyAnimal()
obj.party()
obj.party()
x=20
print(x)