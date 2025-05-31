"""
    Implementare una classe Pacco che comprenda:
    » sei proprietà: numero (int), destinazione (String), peso (int), altezza (int), larghezza (int) e lunghezza (int);
    › numero è un numero intero che rappresenta un codice univoco di identificazione del pacco; il numero viene generato automaticamente (a partire da 1 per il primo pacco e incrementandolo di 1 per ogni nuovo pacco) e non può essere modificato dopo la creazione del pacco;
    destinazione è una stringa che contiene l'indirizzo di destinazione del pacco;
    peso è un numero che indica il peso del pacco [in grammi];
    › altezza, larghezza e lunghezza sono tre numeri che indicano le dimensioni [in cm] del pacco;
    › un costruttore con argomenti sufficienti a inizializzare tutte le proprietà ai valori passati come parametri e di default se non presente  inizializza peso a 1000g e tutte le dimensioni a 100cm;;
    i metodi getter e setter che servono per gestire in maniera adeguata le diverse proprietà secondo le loro caratteristiche (si deve rispettare l'ipotesi che dopo la creazione del pacco sia possibile modificare solo la sua destinazione, mentre le altre proprietà - peso e dimensioni - non
    possono più cambiare).
        Implementare una seconda classe Deposito che viene utilizzata per rappresentare un deposito di smistamento dei pacchi. Si ipotizzi che un deposito non sia in grado di contenere/gestire un numero di pacchi superiore a un valore massimo che deve essere indicato al momento della creazione del deposito. La classe Deposito deve inoltre comprendere:
        » un metodo boolean aggiungiPacco (Pacco p) che aggiunge il pacco p al deposito e che restituisce false se il deposito è pieno e il pacco non può essere inserito (e true nel caso invece che il pacco possa essere aggiunto all'elenco dei pacchi presenti nel deposito);
        » un metodo Pacco trovaPacco (int numeroPacco) che cerca nel deposito il pacco identificato dal numero numeroPacco e ne restituisce il
    riferimento (o null se il pacco non è presente nel deposito);
    » un metodo int quantiPacchi () che restituisce il numero dei pacchi presenti nel deposito;
    » un metodo int quantoPeso () che restituisce il peso complessivo totale dei pacchi presenti nel deposito;
    » un metodo int maxPeso () che restituisce il peso complessivo massimo che è stato conservato nel deposito dal momento della sua creazione;
    » un metodo boolean togliPacco (Pacco p) che toglie il pacco p dal deposito e che restituisce false se il pacco p non è presente nel deposito
    (e true nel caso invece in cui il pacco è presente e viene quindi tolto dal deposito);
    » un metodo boolean togliPacco (int numeroPacco) che toglie dal deposito il pacco identificato dal numero numeroPacco e che restituisce false se il pacco non è presente nel deposito (e true nel caso invece in cui il pacco è presente e viene quindi tolto dal deposito);
    » tutte le proprietà che si ritengono utili ai fini del progetto, con gli opportuni metodi getter e setter;
    » i costruttori (almeno uno) che si ritengono utili ai fini del progetto;
    » un metodo _str_() che restituisce le caratteristiche del deposito e la lista dei pacchi che vi si trovano.
    Completare opportunamente anche il programma di test in modo che arrivi a verificare il corretto funzionamento di tutti i metodi definiti per le classi Pacco e Deposito e che provi a generare un numero di libri sufficienti a verificare tutti i diversi casi previsti.
"""


class Pacco:
    _numerocorrente=1
    def __init__(self,destinazione:str, peso=1000, altezza=100, larghezza=100, lunghezza=100):
        self.__numero= Pacco._numerocorrente
        Pacco._numerocorrente+=1
        self.__destinazione = destinazione
        self.__peso = peso
        self.__altezza= altezza
        self.__larghezza = larghezza
        self.__lunghezza= lunghezza 
        
    def set_destinazione(self,nuova_destinazione):
        self.__destinazione= nuova_destinazione
    def get_destinazione(self):
        return self.__destinazione

    def get_peso(self):
        return self.__peso 
    def get_altezza(self):
        return self.__altezza
    def get_larghezza(self):
        return self.__larghezza
    def get_lunghezza(self):
        return self.__lunghezza 

    def __str__(self):
        return (f"Pacco: {self.__numero}, Destinazione : {self.__destinazione}, Peso: {self.__peso}Kg, Dimensioni: {self.__altezza} x {self.__lunghezza} x {self.__larghezza}cm")



        