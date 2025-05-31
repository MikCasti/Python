def crea_dizionario_traduzioni() -> dict:
    dizionario={}
    numero_parole= int(input("Quante parole vuoi inserire nel dizionario?"))

    for _ in range(numero_parole):
        parola_italiano= input("Inserisci una parola in italiano:")
        parola_inglese= input(f"Inserisci la traduzione in inglee di '{parola_italiano}")
        dizionario[parola_italiano.lower()]= parola_inglese.lower()
    
    return dizionario 

def traduci_parola(dizionario:dict):
    parola_da_tradurre =input("inserisci una parola in italiano da tradurre")

    if parola_da_tradurre in dizionario:
        print(f"La traduzione di '{parola_da_tradurre}'")
    else: 
        print(f"La parola '{parola_da_tradurre}' non esiste nel dizionario ")
        