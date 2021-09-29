import random
#longueur de mots
D={}
s=0
f=open("data.txt","r")
for i in f.read().split():
    if len(i) in D:
        D[len(i)]=D[len(i)]+1
    else:
        D[len(i)]=1
    s=s+1
for i in D:
    D[i]=D[i]/s
f.close()
#premiere lettre de mots
F={}
k=0
f=open("data.txt","r")
for i in f.read().split():
    if i[0].lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        if i[0].lower() in F:
            F[i[0].lower()]=F[i[0].lower()]+1
        else:
            F[i[0].lower()]=1
        k=k+1
for i in F:
    F[i]=F[i]/k
f.close()

longueur_du_mot=random.choices(list(D.keys()), list(D.values()), k=1)
mot=random.choices(list(F.keys()), list(F.values()), k=1)[0]


#enchainement de lettres
f=open("data.txt","r")
labels=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
E={}
for i in labels:
    E[i]={}
for i in E:
    for j in labels:
        E[i][j]=0
chaine=f.read()
f.close()
for i,j in zip(" "+chaine,chaine):
    if i.lower() in labels and j.lower() in labels:
        E[i.lower()][j.lower()]=E[i.lower()][j.lower()]+1
for i in E:
    for j in list(E[i].keys()):
        if sum(list(E[i].values()))!=0:
            E[i][j]=E[i][j]/sum(list(E[i].values()))

for i in range(0,longueur_du_mot[0]-1):
    l=mot[i]
    mot=mot+random.choices(list(E[l].keys()), list(E[l].values()), k=1)[0]

print(mot)


