class PartyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("Current number: ", self.x)

obj=PartyAnimal()
obj.party()
obj.party()