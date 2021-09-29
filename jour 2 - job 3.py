x=int(input("Veuillez renseigner le nombre: "))
s=0
f=open("data.txt","r")
for i in f.read().split():
    if len(i)==x:
        s=s+1
print(s)