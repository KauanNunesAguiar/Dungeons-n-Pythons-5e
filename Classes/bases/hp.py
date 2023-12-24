from recursos import recursos



class vida:
    hp = recursos("Pontos de Vida")
    hp_temp = recursos("Pontos de Vida Temporários", 0, 0)
    dados_vida = recursos("Dados de Vida")
    tipo_dados_vida = "d" + str(0)

    def __init__(self):
        self.hp_conjunto = [self.hp, self.hp_temp]
        self.dados_vida_conjunto = [self.dados_vida, self.tipo_dados_vida]
        
    def set_hp(self, hp):
        self.hp_conjunto[0].set_atual(hp)
        self.hp_conjunto[0].set_maximo(hp)
    
    def set_hp_temp(self, hp_temp):
        self.hp_conjunto[1].set_atual(hp_temp)
        self.hp_conjunto[1].set_maximo(hp_temp)
        
    def set_dados_vida(self, dados_vida, tipo):
        self.dados_vida_conjunto[0].set_atual(dados_vida)
        self.dados_vida_conjunto[0].set_maximo(dados_vida)
        self.dados_vida_conjunto[1] = "d" + str(tipo)
        
    def dano(self, valor):
        hp_temp = self.hp_conjunto[1].get_atual()
        
        if hp_temp >= valor:
            self.hp_conjunto[1].reduzir(valor)
            
        elif hp_temp < valor:
            self.hp_conjunto[0].reduzir(valor - (valor - hp_temp))
            self.hp_conjunto[1].set_atual(0)
            
    def cura(self, valor):
        self.hp_conjunto[0].aumentar(valor)
        
    def cura_temp(self, valor):
        self.hp_conjunto[1].aumentar(valor)
        
    def __repr__(self) -> str:
        return f"{self.hp_conjunto[0].get_nome()}:\n{self.hp_conjunto[0].get_atual()}/{self.hp_conjunto[0].get_maximo()}\n{self.hp_conjunto[1].get_nome()}:\n{self.hp_conjunto[1].get_atual()}/{self.hp_conjunto[1].get_maximo()}\nDados de Vida:\n{self.dados_vida_conjunto[0].get_atual()}{self.dados_vida_conjunto[1]}"
        
            
                
                