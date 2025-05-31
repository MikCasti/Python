#for, stampare i numeri tra 100 e 1000


for i in range(100,1001):
    if i%7==0 and i%13==0 and i%3!=0:
        print(i)


#chiedere all'utente quanti numeri vuole inserire. leggere questi numeri da tastiera e calcolarne la somma dei soli numeri pari. 

i= int(input("Quanti numeri vuoi aggiungere?"))
somma=0
for i in range(i):
    numero=int(input("dimmi il numero"))
    if numero%2==0:
        somma=somma+numero
print(f"somma dei pari: {somma}")

quanti=int(input("quanti numeri vuoi aggiungere "))
somma=0
i=0
while i<quanti:
    numero=int(input("dimmi il numero:")
               if numero%2==0):
    somma=somma+numero
    i+=1
    print(f"Somma dei pari: {somma}")
