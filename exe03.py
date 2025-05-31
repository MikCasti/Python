lista=[1,3,5,7,9,13,15,17,21,71,10,2,6]

numeri= []
quanti=int(input("quanti numeri vuoi?"))
for num in range(quanti):
    valore=int(input("Inserisci un valore:"))
    numeri.append(valore)

somma=0
for i in lista:
    if i%2!=0:
        somma+=i
    if somma>=100: 
        print("Limite superato")
        b





              

