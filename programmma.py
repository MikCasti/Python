"""
Il programma prende in input un file strutturato come prodotto:quantità:prezzo:timestamp_modifica*prodotto:quantità:prezzo:timestamp_modifica, dove ogni parte è separata da : e i prodotti sono separati da *. 
Il programma dovrà estrarre queste informazioni, calcolare il costo totale per ciascun prodotto e infine sommare i costi per ottenere il totale complessivo e le quantità totali di merce presente a magazzino.
Fare un metodo per l'export del magazzino in formato csv (guardare modulo csv)
strutturato come: 
Nome,Quantità,Prezzo,Costo Totale,Ultima Modifica
mela,10,0.5,5.0,2024-11-28
banana,20,0.3,6.0,2024-11-28
arancia,15,0.7,10.5,2024-11-27
pera,30,0.4,12.0,2024-11-28

"""
with open("filepartenza.txt", "r") as file:
    contenuto= file.read()
    

contenuto= contenuto.replace (':',',')
contenuto= contenuto.replace ("*","\n")

print(contenuto)
Quantità= file[1]
Prezzo= file[2]


costototale=Quantità * Prezzo

file.append(costototale)

print(contenuto)






