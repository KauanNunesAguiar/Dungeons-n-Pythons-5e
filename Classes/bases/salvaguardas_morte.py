from recursos import recursos

class salvaguardas_morte:
    def __init__(self, sucessos = 0, falhas = 0):
        self.sucessos = recursos("Sucessos", sucessos, 3)
        self.falhas = recursos("Falhas", falhas, 3)
        
    def set_sucessos(self, sucessos):
        self.sucessos.set_atual(sucessos)
    
    def set_falhas(self, falhas):
        self.falhas.set_atual(falhas)
        
    def add_sucesso(self):
        self.sucessos.aumentar(1)
        if self.sucessos.get_atual() == self.sucessos.get_maximo():
            return True
        else:
            return False
    
    def add_falha(self):
        self.falhas.aumentar(1)
        if self.falhas.get_atual() == self.falhas.get_maximo():
            return True
        else:
            return False
        
    def zerar(self):
        self.sucessos.set_atual(0)
        self.falhas.set_atual(0)
        
    def get_sucessos(self):
        return self.sucessos.get_atual(), self.sucessos.get_maximo()
    
    def get_falhas(self):
        return self.falhas.get_atual(), self.falhas.get_maximo()
    
    def __repr__(self) -> str:
        return f"Sucessos: {self.sucessos.get_atual()}/{self.sucessos.get_maximo()}\nFalhas: {self.falhas.get_atual()}/{self.falhas.get_maximo()}"