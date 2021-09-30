class Livre:

    def __init__(self,titre):
        self.titre=titre

    def print(self):
        print(self.titre)

class Auteur(Livre):

    def __init__(self,name,prenom):
        self.name=name
        self.prenom=prenom
        self.oeuvre=[]

    def listerOeuvre(self):
        print(self.oeuvre)

    def ecrireUnLivre(self,titre):
        livre=Livre(titre)
        self.oeuvre=self.oeuvre+[titre]


p=Auteur("John","Smith")
p.listerOeuvre()
p.ecrireUnLivre("test_titre")
p.listerOeuvre()