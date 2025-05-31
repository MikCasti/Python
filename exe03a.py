#data una lista di numeri, dividi ciasun numero in tre categorie
#positive,negative e zeri

lista=[-1,3,55,0,2,-44,0.55]
positivi=[]
negativi=[]
zeri=[]
for num in lista:
    if num>0:
        positivi.append(num)
    elif num<0:
         negativi.append(num)
    elif num==0:
         zeri.append(num)

print(positivi)
print(negativi)
print(zeri)

sommapositivi=sum(positivi)
print(sommapositivi)

    


