
from ProdottoZ import prodottoZ


class Magazzino:

    def __init__(self,input_string):
        self.__prodotti=self.estrai_prodotti(input_string)

    def estrai_prodotti(self,input_string):
        prodotti=[]
        elementi = input_string.split("*")
        for elemento in elementi:
            parti=elemento.split(":")
            nome=parti[0]
            qta=parti[1]
            prezzo=parti[2]
            timestamp=parti[3]
            prodotto=prodottoZ(nome,qta,prezzo,timestamp)
            prodotti.append(prodottoZ)

        return prodotti 