#parcheggio 
giorno=(input("inserire un giorno della settimaan LUN,MAR,MER,GIO,VEN,SAB,DOM"))
ore=int(input("inserire ore di sosta"))       

def calcolososta(giorno,ore):
    giornisettimana=["LUN","MAR","MER","GIO","VEN"]
    Giorniweekend=["SAB","DOM"]

    if giorno=="sab" or giorno=="dom":
        if ore<=3:
            costo=3
        else:
            costo=3+(ore-3)*0.75
    else: 
        if ore<=2:
            costo=2
        else:
            costo=2+(ore-3)*0.50
            else: costo errato
        return costo

def calcolososta2(giorno,ore,costo):
if isinstance(costo,str):
    print(costo)
else: 
    print(f"Costo: {costo:.2f}") #2 decimali