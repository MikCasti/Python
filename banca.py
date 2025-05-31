import random



class CartadiCredito:
    numero_carta_iniziale = 101101101
    def __init__(self):
        self.__numerocarta=CartadiCredito.numero_carta_iniziale
        CartadiCredito.numero_carta_iniziale +=1
        self.__pin= random.randint(10000, 99999)
        self.__credito= 0
        self.__numoperazioni= 0
 
#getter
    def get_numerocarta(self):
        return self.__numerocarta
    def get_pin(self):
        return self.__pin
    def get_credito(self):
        return self.__credito
    def get_numoperazioni(self):
        return self.__numoperazioni
   
#str
    def __str__(self):
        return f"Carta Numero: {self.__numerocarta} Credito Disponibile: {self.__credito} Operazioni Effettuate: {self.__numoperazioni}"
 
# addebita
    def addebita(self, pin, importo):
        if pin == self.__pin:
            if importo < self.__credito:
                self.__credito -= importo
                self.__numoperazioni += 1
                return f"Operazione Effettuata. Nuovo credito di {self.__credito}"
            else:
                return "Credito Insufficiente"
        return "Pin Errato"
 
#ricarica
    def ricarica(self,importo):
        if importo >0:
            self.__credito += importo
            self.__numoperazioni += 1
        else:
            return "Errore nell'operazione"
        
    