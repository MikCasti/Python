#LISTE

numeri=[1,3,5,7,8]
frutta=["banana","mela","pera"]
misto=["banana",1,"pera",5,7,True,5.6]

print(numeri[2])
print(frutta[2])

print(numeri[1:3])

numeri[1]=99
print(numeri[1])

numeri.append(100) #aggiungiamo alla lista
print(numeri[-1])

numeri.remove(99) 
print(numeri[1])

frase=[]
frase.append("Ciao")
frase.append("a")
frase.append("Tutti")

print(frase)

frase.pop() #elimina l'ultimo elemento della nostra lista
print(frase)

frase.pop(0)
print(frase)

frase.clear() #cancella tutto l'array
print(frase)

lista=["albero","banana","cane"]

for i in lista: #stampa la posizione
    print(i)

for i in range(len(lista)): #stampa la posizione dei valori 
    print(lista[i])

for i in range(len(lista)):
    if i!=0:
        print(lista[i])

pos=lista.index("banana") #returns the position at the first occurrence of the specified value. 
print(pos)

num=[5,2,7,1,99] #ordina la lista in ordine crescente
num.sort()
print(num)

for i,x in enumerate(num): #restituisce 2 valori 
    print(f"indice {i} elemento {x}") 
    



