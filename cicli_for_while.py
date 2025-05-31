#CICLI 

#while
x=0
while x<=5:
    print(x) 
    x+=1  #x=x+1 
i=0
somma=0
while i<10:
    somma=somma+i
   
    i+=1
print(somma)

#for
#for elemento in sequenza: 

for i in range(5): #0 a 4
    print(i)

for i in range(2,10): #2 a 9
    print(i)

print("range passo 2")
for n in range(2,10,2): #2 a 9 con passo 2
    print(n)

print("for parola")
parola="Python"
for lettera in parola:  
    print(lettera)

print ("Break")
#break
#interrompe il ciclo completamente quando viene eseguito
 
for n in range(5):
    #if n==2:
    print(n)
    break

#continue
#lo blocco temporaneamente
for n in range(5):
    if n==3:
        continue
    print(n)
else:
    print("ciclo finito")
    x=0
while x<=5:
    print(x) 
    x+=1  #x=x+1 
else:
    print("ciclo finito")

for i in range(3):
    for j in range(2):
        print(f"{i}, {j}")
#diff tra while e for

#while si basa su una condizione booleana 
#utilizzato quando non si sa a priori quante iterazioni servono

#for
#itera su una sequenza o intervallo di valori noti 
#usato quando il numero di iterazioni è determinato