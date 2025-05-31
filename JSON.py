#JSON è uno dei formati standard, utilizzati per lo scambio dei dati, grazie alla semplicità e leggibilità

#fornisce una serie di funzioni per convertire oggetti python in stringhe JSON

import json

from Classi_Oggetti import Persona


dati={
    "nome":"Mario",
    "eta":30,
    "citta": "Roma"
}

json_string=json.dumps(dati)
print(json_string)
jsonstringa='{"nome":"Pippo","eta":30,"citta":"Busto Arsizio"}'
datijson=json.loads(jsonstringa)
print(datijson)
with open('dati.json','w') as File:
    json.dump(dati,File,indent=4)#perchè come standard si usa tab 

with open('dati1.json','r') as file:
    contenuto=json.loads(file)
print(contenuto)

persone=[
    {"nome":"Paolo","eta":34,"citta":"Milano"},
    {"nome":"Anna","eta":43,"citta":"Legnano"},
    {"nome":"Mario","eta":53,"citta":"Roma"}
]
with open('persone.json','w') as file:
    json.dump(persone,file,indent=4)


with open('persone.json','r') as file:
    personecaricate=json.load(file)
    print(personecaricate)

for p in personecaricate:
    print(f"Nome: {p['Nome']}")


with open("nomi.json","r") as file:
    dati_caricati=json.load(file)
    persone=[Persona(**d) for in dati_caricati]
