#TUPLE
mia_tupla=(1,2,3) #è una collezione di una lista, ma rimane immutabile. quindi non modificabile
print(mia_tupla)
#le tuple sono più performabili 
conta=mia_tupla.count(1)
print(conta)
pos=mia_tupla.index(2)
print(pos)

#DIZIONARI
mio_dizionario={
    "nome":"Mario",
    "età":30,
    "città":"Roma"
}
mio_dizionario["nome"] #ci metto la chiave
print(mio_dizionario["nome"])

print(mio_dizionario)

mio_dizionario["professione"]="panettiere"
print(mio_dizionario)
mio_dizionario["professione"]="Informatico"
print(mio_dizionario)

mio_dizionario.update({"indirizzo":"via roma 1","hobby":"calcio"})
print(mio_dizionario)

mio_dizionario.pop("hobby")
print(mio_dizionario)

del mio_dizionario["indirizzo"]
print(mio_dizionario)
 
mio_dizionario.popitem() #removes the item that was last inserted into the dictionary
print(mio_dizionario)

mio_dizionario.clear()
print(mio_dizionario)

for chiave in mio_dizionario:
    print(chiave)

for valore in mio_dizionario:
    print(valore)

for chiave,valore in mio_dizionario:
    print(f"chiave:{chiave} e valore: {valore}")

for chiave in mio_dizionario.keys(): #returns a view object
    print(chiave)

professione=mio_dizionario.get("professione","disoccupato") #returns the value of the item with the specified key.
print(professione)



