class Persona:

    def __init__(self,nome,eta):
        self.__nome= nome 
        if eta<0:
                raise Exception("Errore in eta")
        self.__eta=eta

