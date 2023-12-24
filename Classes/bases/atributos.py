class atributos:
    def __init__(self, nome: str, valor = 10):
        self.nome = nome
        self.valor = valor
        self.set_modificador()
    
    def set_nome(self, nome):
        self.nome = nome
        
    def set_valor(self, valor):
        if valor < 1:
            self.valor = 1
        else:
            self.valor = valor
            self.set_modificador()
            
    def set_modificador(self):
        self.modificador = (self.valor - 10) // 2
        
    def get_nome(self):
        return self.nome
    
    def get_valor(self):
        return self.valor
    
    def get_modificador(self):
        return self.modificador

    def __repr__(self) -> str:
        return f"{self.nome}: {self.valor} ({self.modificador})"

        
    