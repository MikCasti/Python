class prodotto:
    def __init__(self,nome,quantita,prezzo,timestamp):
        self.__nome=nome
        self.__quantita=quantita
        self.__prezzo=prezzo
        self.__timestamp=timestamp

    def costo_totale(self):
        return self.__prezzo*self.__quantita
    


    
    