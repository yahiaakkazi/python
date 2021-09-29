import matplotlib.pyplot as plt

f=open("data.txt","r")
labels=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
D={}
for i in labels:
    D[i]={}
for i in D:
    for j in labels:
        D[i][j]=0
chaine=f.read()
f.close()
for i,j in zip(" "+chaine,chaine):
    if i.lower() in labels and j.lower() in labels:
        D[i.lower()][j.lower()]=D[i.lower()][j.lower()]+1
for i in D:
    for j in list(D[i].keys()):
        if sum(list(D[i].values()))!=0:
            D[i][j]=D[i][j]/sum(list(D[i].values()))
print(D)
for i in range(0,len(labels)):
    plt.plot(list(D.keys()), list(list(D.values())[i].values()), label=labels[i])
plt.legend(title='letters occurences')
plt.show()

