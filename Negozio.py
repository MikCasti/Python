from exe05a import CapoAbbigliamento
from Negozio import Negozio

class Negozio: 
    def __init__(self,nome):
        self.__nome=nome
        self.__prodotti=[]
    def aggiungiCapo(self,prodotto:CapoAbbigliamento):
        self.__prodotti.append(prodotto)
    
    def stampaesistenze(self):
        esistenze="Esiste:\n"  
        for prodotto in self.__prodotti:
            esistenze+=str(prodotto) #renderà i get dettagli in una stringa
        return esistenze
    def totalquantità(self):
        totale=0
        for prodotto in self.__prodotti: 
            totale+=prodotto.get_qta() #+= mi permette di incrementare 
        return totale
    

