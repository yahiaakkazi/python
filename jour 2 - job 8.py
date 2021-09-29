import matplotlib.pyplot as plt
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
plt.bar(list(D.keys()), D.values(), color="g")
plt.show()
