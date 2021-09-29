import matplotlib.pyplot as plt
D={}
s=0
f=open("data.txt","r")
for i in f.read().split():
    if i[0].lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
        if i[0].lower() in D:
            D[i[0].lower()]=D[i[0].lower()]+1
        else:
            D[i[0].lower()]=1
        s=s+1
for i in D:
    D[i]=D[i]/s
f.close()
plt.bar(list(D.keys()), D.values(), color="g")
plt.show()