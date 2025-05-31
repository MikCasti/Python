from pacco import Pacco


class Deposito: 
    
    def __init__(self, capacita):
        self.__capacita= capacita
        self.pacchi = []
        self.peso_totale = 0 
        self.max_peso=0

    
    def aggiungi_pacco(self,pacco):
        if len(self.__pacchi) < self.__capacita:
            self.pacchi.append(pacco)
            self.peso_totale+=pacco.get_peso()
            self.__max_peso=max(self.__max_peso,self.peso_totale)
            return True
        return False
    
    def trova_pacco(self,numeroPacco:int)->Pacco:
        for pacco in self.__pacchi:
            if pacco.get_numero() == self.__numeroPacco: 
                return pacco 
            return None
    def quantiPacchi (self):
        return len(self.__pacchi)
    def quantoPeso (self):
        return self.__max_peso
    def togliPacco(self,pacco):
        if pacco in self.__pacchi:
            self.__pacchi.remove(pacco)
            self.peso_totale-=pacco.get_peso()
            return True
        return False
    def ToglipaccoPerNumero(self,numero):
        pacco=self.cercaPacco(numero)
        if pacco:
            return self.togliPacco(Pacco)
        return False
    def __str__(self):
        st=""
        for pacco in self.__pacchi:
            str +=str(pacco)
            
        
    

        
    



