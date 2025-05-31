class Persona: 
    def __init__(self,nome, age): 
        self.__nome= nome
        self.__age= age
    def saluta(self):
        print(f"Ciao sono {self.__nome} e ho  {self.__age}anni")

class Studente(Persona):
    def __init__(self, nome, age, matricola):
        super().__init__(nome, age)
        self.__matricola = matricola
    def info_studente(self):
        print(f"Studente matricola:")
    def saluta(self):
        print(f"sono uno studente con matricola: {self.__matricola}")
