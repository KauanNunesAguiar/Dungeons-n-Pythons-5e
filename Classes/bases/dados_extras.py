class dados_extras:
    def __init__(self, inspiracao, proficiencia, ca, iniciativa, deslocamento):
        self.inspiracao = inspiracao
        self.proficiencia = proficiencia
        self.ca = ca
        self.iniciativa = iniciativa
        self.deslocamento = deslocamento
        
    def set_inspiracao(self, inspiracao):
        self.inspiracao = inspiracao
        
    def set_proficiencia(self, proficiencia):
        self.proficiencia = proficiencia
        
    def set_ca(self, ca):
        self.ca = ca
        
    def set_iniciativa(self, iniciativa):
        self.iniciativa = iniciativa
        
    def set_deslocamento(self, deslocamento):
        self.deslocamento = deslocamento
        
    def get_inspiracao(self):
        return self.inspiracao
    
    def get_proficiencia(self):
        return self.proficiencia
    
    def get_ca(self):
        return self.ca
    
    def get_iniciativa(self):
        return self.iniciativa
    
    def get_deslocamento(self):
        return self.deslocamento