#commessa
class CapoAbbigliamento: #nome classe sempre maiuscolo


    _numeroprogressivo=1

   
    def __init__(self,capo:str,marca:str,prezzo:float,taglia:str,quantità:int):
        self.__capo = capo 
        self.__marca = marca
        self.__prezzo = prezzo
        self.__taglia = taglia
        self.__quantità = quantità 

        self.__barcode=CapoAbbigliamento.__numero_progressivo
        CapoAbbigliamento.__numero_progressivo+=1
    
    #metodi getter(lettura) e setter (scrittura)
    def get_capo(self):
        return self.__capo
    def get_marca(self):
        return self.__marca
    def get_prezzo(self):
        return self.__prezzo
    def get_taglia(self):
        return self.__quantità
    def get_quantità(self):
        return self.__quantità
    def set_tipo(self,capo):
        self.__capo=capo
    def stampacosto(self):
        print(f"Costo prodotto {self.__capo} è {self.__prezzo}")
    def cambiaprezzo(self,prezzo):
        if prezzo>0:
                self.__prezzo=prezzo
    def applicasconto(self,sconto):
        if sconto>0:
            prezzoscontato=self.__prezzo*(1-sconto/100)
            self.__prezzo=prezzoscontato
    def venditeCapo(self,quantità):
        if self.quantità>0:
            self.__quantità-=1 #perche se no va in negativo, quindi si mette -=
            return "Capo Venduto"
        else:
            return "Capo non venduto quantità insufficiente"
        
    def incrementequantità(self,quantitàincremento):
        if quantitàincremento>0:
            self.__quantità+=quantitàincremento
    def getdettagli (self):
        dettagli= "Capo Abbigliamento barcode=%d capo=%s marca=%s prezzo=%f taglia=%s quantità=%d" %(self.__barcode, self.__capo,self.__prezzo,self.__quantità)
        return dettagli
    

    
    