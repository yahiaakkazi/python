class Personne:
    def __init__(self, name, prenom):
        self.name = name
        self.prenom = prenom

    def sePrésenter(self):
        print(self.name,self.prenom)

p1=Personne("John","Smith")
p2=Personne("Alex","alex")
p3=Personne("Jogn","John")

for i in [p1,p2,p3]:
    i.sePrésenter()

