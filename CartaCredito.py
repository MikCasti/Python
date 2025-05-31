"""
Implementare una classe CartaCreditoRicaricabile che comprenda:
» quattro proprietà: numeroCarta (int), PIN (int), creditoDisponibile (int), numOperazioni (int),;
» un solo costruttore senza parametri che inizializza:
› numerocarta a un valore univoco che viene assegnato partendo da 101 101 101 e viene progressivamente incrementato (per cui la prima carta generata avrà numero uguale a 101 101 101, la seconda 101 101 102, la terza 101 101 103 e così via). Si ricordi che, una volta generato dal costruttore, il numero della carta non può più essere modificato;
› PIN a un numero intero compreso tre 10 000 e 99 999, generato a caso. Anche in questo caso, una volta generato dal costruttore, il PIN non è più modificabile;
› creditoDisponibile a zero. Il credito potrà essere modificato solo attraverso apposita operazioni di addebito (che comporta una diminuzione del credito disponibile) o di ricarica (che comporta un incremento del credito disponibile);
› numoperazioni a zero. Questa proprietà deve tener conto delle operazioni (ricariche o addebiti) effettuate sulla carta, quindi potrà essere soltanto incrementata di una unità ogni volta che viene effettuata un'operazione;
» un metodo none ricarica (int importo) che registra una ricarica della carta e che incrementa il credito disponibile sulla carta dell'importo
indicato come parametro dell'operazione;
» un metodo boolean addebita (int PIN, int importo) che, nel caso il credito disponibile sulla carta sia sufficiente e il PIN indicato sia proprio quello della carta corrente, registra una operazione di addebito sulla carta. Se il credito disponibile è uguale o superiore all'importo, allora viene registrata l'operazione, il credito disponibile viene diminuito dell'importo e viene restituito un risultato positivo (true). Se invece il credito disponibile è inferiore all'importo richiesto, allora l'operazione non viene registrata, il credito non viene modificato e viene restituito un risultato negativo (false). Analogamente, se il PIN inserito non è uguale a quello registrato per la carta corrente l'operazione non viene effettuata e quindi non viene nemmeno registrata;
» i metodi getter di tutte le proprietà (si noti che i setter sono esplicitamente esclusi dalle specifiche indicate sopra);
» un metodo __str__ che provveda a restituire una stringa analoga alla seguente:
Carta Numero 101101101, credito disponibile: 2000, operazioni effettuate: 5.
"""

import random
_numeroprogressivo=1

class CartaCredito:
    numero_carta_iniziale=101101101
    def __init__(self,numeroCarta:int,PIN:int,creditoDisponibile:int,numOperazioni:int):
        self.__creditoDisponibile= 0
        self.__numOperazioni= 0
        self.__numeroCarta=CartaCredito.numero_carta_iniziale
        CartaCredito.numero_carta_iniziale+=1
        self.__PIN=random.randit(10000,99999)
    def get_CreditoDisponibile(self):
        return self.__creditoDisponibile
    def Addebito(self,pin,importo): 
        if pin==self.__PIN: 
            self.__creditoDisponibile-= importo
            self.__numOperazioni=1
        else:
            print("Credito insufficiente")
    def ricarica(self,pin,importo):
        if pin==self.__PIN:
            self.__creditoDisponibile+=importo
            self.__numOperazioni=1
    def __str__(self):
        return f"Carta credito: {self.__numeroCarta} credito {self.__creditoDisponibile} operazioni: {self.__numOperazioni}"
    
    
        

