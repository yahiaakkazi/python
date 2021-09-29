import matplotlib.pyplot as plt

labels= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
D={}
for i in labels:
    D[i]=0
s=0
f=open("data.txt","r")
for i in f.read():
    if i.lower() in labels:
        D[i.lower()]=D[i.lower()]+1
        s=s+1
for i in D:
    D[i]=D[i]/s

f.close()
plt.bar(list(D.keys()), D.values(), color='g')
plt.show()

