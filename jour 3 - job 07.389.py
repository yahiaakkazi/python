class Personne:
    def __init__(self, name, prenom):
        self.name = name
        self.prenom = prenom

    def sePrésenter(self):
        print(self.name,self.prenom)

class Client(Personne):

    def __init__(self,name,prenom):
        self.name=name
        self.prenom=prenom
        self.collection=[]

    def inventaire(self):
        return(self.collection)

    def ajouter_dans_sa_collection(self,titre):
        self.collection=self.collection+[titre]

    def supprimer_sa_collection(self):
        self.collection=[]



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
        return(self.oeuvre)

    def ecrireUnLivre(self,titre):
        livre=Livre(titre)
        self.oeuvre=self.oeuvre+[titre]

p=Auteur("John","Smith")
p.ecrireUnLivre("test_titre")

class Bibliotheque:

    def __init__(self,nom,catalogue):
        self.nom= nom
        self.catalogue= catalogue

    def inventaire(self):
        print(self.catalogue)

    def louer(self,client,nom_livre):
        self.nom_livre=nom_livre
        if nom_livre in self.catalogue:
            if self.catalogue[nom_livre]>0:
                client.ajouter_dans_sa_collection(nom_livre)
                self.catalogue[nom_livre]=self.catalogue[nom_livre]-1

    def rendreLivres(self,client):
        for i in client.inventaire():
            if i in self.catalogue:
                self.catalogue[i]=self.catalogue[i]+1
            else:
                self.catalogue[i]=1
        client.supprimer_sa_collection()

    def acheterLivre(self,auteur,nom_livre,quantite_du_livre):
        self.nom_livre=nom_livre
        self.quantite_du_livre= quantite_du_livre
        if self.nom_livre in auteur.listerOeuvre():
            self.catalogue[self.nom_livre]=self.quantite_du_livre

b=Bibliotheque("Bibilio",{'Titre x': 2, 'Titre y': 3})

#Nous allons créer deux auteurs, qui ont écrit un livre chacun, deux bibliothèques vont acheter leurs livres, et deux clients vont louer leurs oeuvres
auteur1=Auteur("Mike","Erhm")
auteur1.ecrireUnLivre("1er livre de Mike")
auteur2=Auteur("Bryan","W")
auteur2.ecrireUnLivre("1er livre de W")
b1=Bibliotheque("Bibilo1 qui va acheter le livre de Mike",{})
b1.acheterLivre(auteur1,"1er livre de Mike",2)
b2=Bibliotheque("Bibilo1 qui va acheter le livre de W",{})
b2.acheterLivre(auteur2,"1er livre de W",33)

c1=Client("Fring","Hank")
c2=Client("Skyler","Mitte")

b1.louer(c1,"1er livre de Mike")
b2.louer(c2,"1er livre de W")


