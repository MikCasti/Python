 
class AccountBancario: 
    def __init__(self,nomeCliente:int, numeroConto:int,saldo:float=0):
          self.__nomeCliente = nomeCliente = nomeCliente 
          self.__numeroConto = numeroConto = numeroConto 
          self.__saldo = saldo
    def get_nomecliente(self):
          return self.__nomeCliente
    def get_numeroconto(self):
          return self.__numeroConto
    def get_Saldo(self):
          return self.__saldo
    def deposito(self,importo):
          if importo>0:
            self.__saldo=self.__saldo+importo
    def prelievo(self,importo):
            if importo<=0:
                  print("Errore")
           
            elif importo > self.__saldo:
                  print("Prelievo effettuato") 
            else: importo< self.__saldo
            print("Prelievo non effettuabile")
    def get_saldo(self):
        return self.__saldo
        print("Saldo Aggiornato:")
    def VisualizzaInfo(self):
          print(f"{self.nomeCliente},{self.numeroConto},{self.saldo}")
 
          
            
        

          
          
     
