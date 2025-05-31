#parcheggio 
tariffa= float(input("Inserisci le ore nel parcheggio"))
Extra=float(input("Inserisci le ore aggiuntive"))


print(f"{tariffa}")
print(f"{Extra}")

def tariffa(GiorniLavorativi,GiorniFestivi,Oreaggiuntive):
    GiorniLavorativi="Lunedi","Martedi","Mercoledi","Giovedi","Venerdi"
    GiorniFestivi="Sabato","Domenica"
    if tariffa<2 in GiorniLavorativi:
        print(f"il prezzo è di 2 euro")
    elif tariffa>2: 
        print(f"il prezzo è di {tariffa+0.50*Oreaggiuntive}")


