from classes.bases.atributos import atributos
# from classes.bases.salvaguardas_morte import salvaguardas_morte
from classes.bases.hp import vida

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
        repr_atributos_base = f"Atributos Base:\n{self.atributos_base[0]}\n{self.atributos_base[1]}\n{self.atributos_base[2]}\n{self.atributos_base[3]}\n{self.atributos_base[4]}\n{self.atributos_base[5]}\nAtributos Temporários:\n{self.atributos_temp[0]}\n{self.atributos_temp[1]}\n{self.atributos_temp[2]}\n{self.atributos_temp[3]}\n{self.atributos_temp[4]}\n{self.atributos_temp[5]}"
        return f"Nome: {self.nome}\n{self.vida}\n{repr_atributos_base}"