x=10
confronto=x>5

if confronto:
    print("x maggiore di 5")
    print("fine programma")

if x>5:
    print("x maggiore di 5")
else:
    print("non è maggiore 5")



n=5

if n>10:
    print("n maggiore di 10")
elif n==5:
    print("n è uguale a 5")
else: print("n non è maggiore di 10 ne uguale a 5")

età=20

if età>18 and età<30:
    print("hai un età compresa tra 19 e 29")

b=False
if not b:
    print("b è false")

giorno="sabato"
if giorno=="sabato" or giorno=="domenica":
    print("festa per il weekend")

#Ternary operator: espressione if inline permette di scrivere una condizione su una singola linea
    #risultato = "positivo" if x>10 else "Negativo"

n=5 
risultato="Positivo" if n>0 else "Negativo"
print(risultato)


n=int(input("Definisci un valore"))
if n>0:
    print("positivo")
elif n==0:
    print("uguale a 0")
else: print("negativo" )


età=int(input("Inserisci l'età"))
if età>0 and età<18:
    print("Minorenne")
elif età>18:
    print("maggiorenne")
elif età<=0 or età==0:
    print("Nn valido")

else: print("Buon 18esimo")

n2=10
if n2%2==0 and n2%3==0:
    print("pari")
else:
    print("dispari")




