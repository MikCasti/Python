"""
#RAISE
try:

    parola= input ("metti una parola")
    raise ValueError("Errore manuale!")
except ValueError:
    print("Hai fatto un value error")

    """
#CLASSI E OGGETTI PYTHON 
#è un modello per creare oggetti in python
class Persona:

    specie="Umana"

   #costruttore per inizializzare gli attributi
    def __init__(self,nome:str, età:int):
        self.__nome = nome #attributo della classe
        self.__eta = età #attributo della classe
    def saluta(self):
        print(f"Ciao mi chiamo {self.nome} e ho {self.eta}")

    def get_nome(self):
        return self.__nome
    def get_eta(self):
        return self.__eta
    def self_nome(self,nome):
        self.__nome=nome
    def self_età(self,eta):
        self.__eta=eta

 # Output: Luca 25
#self è un riferimento all'istanza ed è utilizzato per 
#accedere agli attributi e metodi definiti nella classe


mario = Persona("Mario",30)
pippo=Persona("Pippo",35)

print(mario.get_eta())
print(pippo.get_nome())

print(pippo.specie)

pluto=Persona("Pluto")
pluto.saluta()

#Metodi: funzioni

pippo.set_nome=("Pasquale")
pippo.saluta()



print("Fine")
