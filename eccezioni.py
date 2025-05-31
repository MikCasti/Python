#eccezioni: è un evento che si verifica durante
#l'esecuazione di un programma e che interrompe il flusso del prog.

try:
    n=7/2
    print(f"passo:{n}")
except ZeroDivisionError:
    print("Si è verificato un errore")
print("fine")
#try and except
#except intercetta l'errore
#finally viene eseguito anche se c'è un errore

a=[4,7,8,9]
try:
    print(a[5])
except IndexError:
    print("Indice oltre i limiti")
try:
    m=int(input("inserisci un valore:"))

    divisione=10/m
    print(divisione)
except ValueError:
    print("non hai inserito un numero")
except ZeroDivisionError:
        print("Hai diviso un numero per 0")
else: 
    print(f"Risultato {divisione}")
finally:
     print("fine programma")
    
    