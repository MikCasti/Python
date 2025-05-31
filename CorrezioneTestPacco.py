
from correzioneDeposito import Deposito
from correzionePACCO import Pacco


def test():
    # Creazione dei pacchi
    pacco1 = Pacco(destinazione="Milano", peso=2000, altezza=50, larghezza=30, lunghezza=20)
    pacco2 = Pacco(destinazione="Roma", peso=1500)
    pacco3 = Pacco(destinazione="Torino", peso=500)

    print(pacco1)
    print(pacco2)
    print(pacco3)

    # Creazione del deposito
    deposito = Deposito(capacita_massima=2)

    # Test aggiunta pacchi
    print("\nAggiunta pacchi:")
    print(deposito.aggiungiPacco(pacco1))  # True
    print(deposito.aggiungiPacco(pacco2))  # True
    print(deposito.aggiungiPacco(pacco3))  # False (deposito pieno)

    print("\nSituazione deposito:")
    print(deposito)

    # Test ricerca pacchi
    print("\nRicerca pacco #1:")
    trovato = deposito.trovaPacco(1)
    print(trovato if trovato else "Pacco non trovato")

    # Test rimozione pacco
    print("\nRimozione pacco #1:")
    print(deposito.togliPaccoNumero(1))  # True
    print("\nSituazione deposito:")
    print(deposito)

    # Test pesi
    print("\nPeso complessivo deposito:")
    print(deposito.quantoPeso())

    print("\nPeso massimo registrato:")
    print(deposito.maxPeso())


# Esegui il test
test()