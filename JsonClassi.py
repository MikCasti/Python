import json
class prodottiJson:
    def __init__(self, product_id:int, nome:str, features:str):
        self.__product_id= product_id
        self.__nome= nome 
        self.__features= features

    def get_product_id(self):
        return self.__product_id
    def get_nome(self):
        return self.__nome
    def get_features(self):
        return self.__features
    
    def __str__(self):
        return f"prodottiJson(product_id={self.__product_id},nome={self.__nome},features={self.__features})"
    
    