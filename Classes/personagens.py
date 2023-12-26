from ast import mod
from classes.bases.habilidades import habilidades
from classes.bases.hp import vida

class personagem:
    lista_personagens = []
    
    def __init__(self, nome: str, hp: vida = vida(), habilidades_base: habilidades = habilidades(), habilidades_temp: habilidades = habilidades()):
        self.nome = nome
        self.hp = hp
        self.habilidades_base = habilidades()
        self.habilidades_temp = habilidades()

        self.lista_personagens.append(self)
        
    def set_nome(self, nome: str):
        self.nome = nome
    
    def set_hp(self, hp: vida):
        self.hp = hp
        
    def set_habilidades(self, habilidades: habilidades):
        self.set_habilidades_base(habilidades)
        self.set_habilidades_temp(habilidades)
        
    def set_habilidades_base(self, habilidades_base: habilidades):
        self.habilidades_base = habilidades_base
        
    def set_habilidades_temp(self, habilidades_temp: habilidades):
        self.habilidades_temp = habilidades_temp
        
    def get_modificador_pericia(self, pericia: str):
        if pericia in self.habilidades_temp.get_pericias():
            modificador = self.habilidades_temp.get_modificador_pericia(pericia)
        else:
            modificador = None
            
        return modificador
    
    def get_modificador_salvaguarda(self, salvaguarda: str):
        if salvaguarda in self.habilidades_temp.get_salvaguardas():
            modificador = self.habilidades_temp.get_modificador_salvaguarda(salvaguarda)
        else:
            modificador = None
            
        return modificador
        
    def faz_teste_salvaguarda(self, salvaguarda: str):
        modificador = self.get_modificador_salvaguarda(salvaguarda)
        if modificador != None:
            return modificador
        else:
            return None
        
    def faz_teste_pericia(self, pericia: str):
        modificador = self.get_modificador_pericia(pericia)
        if modificador != None:
            return modificador
        else:
            return None
        
    def get_nome(self):
        return self.nome
    
    def get_hp(self):
        return self.hp
    
    def get_habilidades_base(self):
        return self.habilidades_base
    
    def get_habilidades_temp(self):
        return self.habilidades_temp
    
    def __repr__(self) -> str:
        return f"Nome: {self.nome}\n{self.hp}\nHabilidades Base:\n{self.habilidades_base}\nHabilidades Temporárias:\n{self.habilidades_temp}"