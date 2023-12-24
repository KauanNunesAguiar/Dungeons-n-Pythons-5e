from numpy import rec


class recursos:
    def __init__(self, nome: str, atual = 1, maximo = 1):
        self.nome = nome
        self.atual = atual
        self.maximo = maximo
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_atual(self, atual):
        self.atual = atual
        
    def set_maximo(self, maximo):
        self.maximo = maximo
        
    def reduzir(self, valor):
        if self.atual - valor < 0:
            self.atual = 0
        else:
            self.atual -= valor
    
    def aumentar(self, valor):
        if self.atual + valor > self.maximo:
            self.atual = self.maximo
        else:
            self.atual += valor
            
    def get_nome(self):
        return self.nome
    
    def get_atual(self):
        return self.atual
    
    def get_maximo(self):
        return self.maximo
    
    def __repr__(self) -> str:
        return f"{self.nome}: {self.atual}/{self.maximo}"

pc = recursos("Peças de Cobre", 0, 0)
pp = recursos("Peças de Prata", 0, 0)
pe = recursos("Peças de Eletrum", 0, 0)
po = recursos("Peças de Ouro", 0, 0)
pl = recursos("Peças de Platina", 0, 0)

esp_mag_0 = recursos("Espaços de Truques", 0, 0)
esp_mag_1 = recursos("Espaços de 1º Nível", 0, 0)
esp_mag_2 = recursos("Espaços de 2º Nível", 0, 0)
esp_mag_3 = recursos("Espaços de 3º Nível", 0, 0)
esp_mag_4 = recursos("Espaços de 4º Nível", 0, 0)
esp_mag_5 = recursos("Espaços de 5º Nível", 0, 0)
esp_mag_6 = recursos("Espaços de 6º Nível", 0, 0)
esp_mag_7 = recursos("Espaços de 7º Nível", 0, 0)
esp_mag_8 = recursos("Espaços de 8º Nível", 0, 0)
esp_mag_9 = recursos("Espaços de 9º Nível", 0, 0)