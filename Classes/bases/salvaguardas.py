import struct
from classes.bases.salvaguardas_morte import salvaguardas_morte

class salvaguardas:
    def __init__(self, nome: str, valor: bool):
        self.nome = nome
        self.valor = valor
    
    def set_nome(self, nome: str):
        self.nome = nome
        
    def set_valor(self, valor: bool):
        self.valor = valor
        
    def get_nome(self):
        return self.nome
    
    def get_valor(self):
        return self.valor
    
    def __repr__(self) -> str:
        return f"{self.nome}: {self.valor}"
    

class pericias_a:
    lista_pericias = []
    lista_salvaguardas = []
    def __init__(self, salvaguardas: list, pericias: list, morte: salvaguardas_morte):
        self.salvaguardas = salvaguardas
        self.pericias = pericias
        self.morte = morte
        
    def set_lista_salvaguardas(self, lista_salvaguardas):
        