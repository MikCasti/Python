"""
esercizio per casa
dizionario italiano inglese
chiedere all'utente quante parole vuole inserire: numero
italiano ----> inglese
chiedere all'utente di inserire  una parola in italiano e vi stamperà la traduzione in inglese se non esiste gli comunicate che non esiste
crea_dizionario_traduzioni: input numero di parole e le parole italiano inglese
-> dict
traduci_parole(dizionario): chiedere la parola da tradurre e stamparla
"""
num=int(input("Inserisci quante parole vuoi inserire:"))
Dizionario={}
italiano=input("inserisci la parola in italiano:")
inglese=input("inserisci la parola in inglese:")
Dizionario[italiano]=inglese
print(Dizionario)
if italiano==Dizionario and inglese==Dizionario:
    print(f"Caricamento")
else: print(f"Non presente")
traduzione = Dizionario.get (italiano, "La parola è:")
print(f"La traduzione di {italiano} è: '{traduzione}'")