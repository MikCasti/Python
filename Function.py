#function: è un blocco di codice riutilizzabile che esegue una 
#determinata operazione. 

"""
utilizzate per suddividere un programma in moduli più piccoli 
rendendo il codice più facile da leggere gestire e utilizzare

def: nome_funzione(parametri):
#blocco di codice da eseguire 
return risultato #Restitiuisce un valore opzionale

parametri: sono nomi di variabili
argomento: valore reale passata alla funzione
ex. 
def saluta(nome): # 'nome' è il parametro 
print(f"Ciao, (nome)!")
saluta("Mario) #"Mario" è l'argomento
#output: Ciao,Mario!
"""

def saluta(nome):
    print(f"Ciao {nome}")

def moltiplica(a,b):
    molt=a*b
    return molt
nome1="Mario"
saluta(nome1)

#parametri posizionali
m1=5.5
m2=6
risultato=moltiplica(m1,m2)
print(risultato)

#valori di default
def saluta_persona(nome="Utente"):
    print(f"Ciao {nome}")

saluta_persona("Pippo")

#parametri keyword
def descrizione_animale(tipo,nome):
    print(f"L'animale è di tipo {tipo} e si chiama {nome}")

descrizione_animale(nome="Fido",tipo="Cane")

#parametri variabili (*args e **kwargs)

def somma(*numeri):
    sommanumeri=sum(numeri)
    return sommanumeri
    print(sommanumeri)

#permette di passare un numero variabile di argomenti per nome
def informazioni(**dettagli):
    for chiave,valore in dettagli.items():
        print(f"{chiave} : {valore}")

informazioni(nome="Pippo",età=55,città="Milano")

#con valori di ritorno 
def operazioni(a,b):
    differenza=a-b
    somma=a+b
    return(somma,differenza)

diff,somm=operazioni(5,3)
print (diff)
print(somm)

#senza valori di ritorno
prova=saluta("Mario")
print(prova)
saluta ("Mario")

def moltiplica(a:int,b:int) -> int:
    molt=a*b
    return molt 

def ispari2(n:int)->bool:
    if n%2==0:
        return True
    else:
        return  False
pari=ispari2(5)
print(pari) 

#max,,avg,min

num=[3,6,7,2,1]
massimo=max(num)
print(massimo)
minimo=min(num)
print(minimo)
