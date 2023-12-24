from Classes.bases.atributos import atributos
# from Classes.bases.salvaguardas_morte import salvaguardas_morte
from Classes.bases.hp import vida

class personagem:
    lista_personagens = []
    forca = atributos("Força")
    destreza = atributos("Destreza")
    constituicao = atributos("Constituição")
    inteligencia = atributos("Inteligência")
    sabedoria = atributos("Sabedoria")
    carisma = atributos("Carisma")
    
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = vida()
        self.atributos_base = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        self.atributos_temp = self.atributos_base.copy()
        
        self.lista_personagens.append(self)
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_atributos_base(self, atributos_base):
        self.atributos_base = atributos_base
        
    def set_atributos_temp(self, atributos_temp):
        self.atributos_temp = atributos_temp
        
    def get_nome(self):
        return self.nome
    
    def get_atributos_base(self):
        return self.atributos_base
    
    def get_atributos_temp(self):
        return self.atributos_temp
    
    def __repr__(self) -> str:
        return f"Nome: {self.nome}\n{self.vida}\nAtributos Base:\n{self.atributos_base}\nAtributos Temporários:\n{self.atributos_temp}"
    