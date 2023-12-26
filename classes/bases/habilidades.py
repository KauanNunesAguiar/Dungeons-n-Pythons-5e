# Dicionario de atributos
# nome: [valor, modificador]
atributos = {
    "Força": [10, 0],
    "Destreza": [10, 0],
    "Constituição": [10, 0],
    "Inteligência": [10, 0],
    "Sabedoria": [10, 0],
    "Carisma": [10, 0]
}

# Dicionario de salvaguardas
# nome: proficiente
salvaguardas = {
    "Força": False,
    "Destreza": False,
    "Constituição": False,
    "Inteligência": False,
    "Sabedoria": False,
    "Carisma": False
}

# Dicionario de pericias
# nome: [atributo, proficiente, modificador]
pericias = {
    "Acrobacia": ["Destreza", False],
    "Arcanismo": ["Inteligência", False],
    "Atletismo": ["Força", False],
    "Atuação": ["Carisma", False],
    "Enganação": ["Carisma", False],
    "Furtividade": ["Destreza", False],
    "História": ["Inteligência", False],
    "Intimidação": ["Carisma", False],
    "Intuição": ["Sabedoria", False],
    "Investigação": ["Inteligência", False],
    "Lidar com Animais": ["Sabedoria", False],
    "Medicina": ["Sabedoria", False],
    "Natureza": ["Inteligência", False],
    "Percepção": ["Sabedoria", False],
    "Persuasão": ["Carisma", False],
    "Prestidigitação": ["Destreza", False],
    "Religião": ["Inteligência", False],
    "Sobrevivência": ["Sabedoria", False]
}

class habilidades:
    def __init__(self, atributos: dict = atributos, proficiencia: int = 0, salvaguardas: dict = salvaguardas, pericias: dict = pericias):
        self.atributos = atributos.copy()
        self.proficiencia = proficiencia
        self.salvaguardas = salvaguardas.copy()
        self.pericias = pericias.copy()
        
        self.calcular_modificadores_atributos()
    
    def set_atributos(self, atributos: dict):
        self.atributos = atributos.copy()
        self.calcular_modificadores_atributos()
        
    def set_proficiencia(self, proficiencia: int):
        self.proficiencia = proficiencia
        
    def set_salvaguardas(self, salvaguardas: dict):
        self.salvaguardas = salvaguardas.copy()
        
    def set_pericias(self, pericias: dict):
        self.pericias = pericias.copy()
        
    def calcular_modificadores_atributos(self):
        for atributo in self.atributos:
            self.atributos[atributo][1] = (self.atributos[atributo][0] - 10) // 2
        
    def get_atributos(self):
        return self.atributos
    
    def get_proficiencia(self):
        return self.proficiencia
    
    def get_salvaguardas(self):
        return self.salvaguardas
    
    def get_pericias(self):
        return self.pericias
    
    def get_modificador_salvaguarda(self, salvaguarda: str):
        if salvaguarda in self.salvaguardas:
            if self.salvaguardas[salvaguarda]:
                return self.atributos[salvaguarda][1] + self.proficiencia
            else:
                return self.atributos[salvaguarda][1]
        else:
            return None
        
    def get_modificador_pericia(self, pericia: str):
        if pericia in self.pericias:
            if self.pericias[pericia][1]:
                return self.atributos[self.pericias[pericia][0]][1] + self.proficiencia
            else:
                return self.atributos[self.pericias[pericia][0]][1]
        else:
            return None
    
    def __copy__(self):
        return habilidades(self.atributos, self.proficiencia, self.salvaguardas, self.pericias)
    
    def __repr__(self) -> str:
        return f"Atributos: {self.atributos}\nProficiência: {self.proficiencia}\nSalvaguardas: {self.salvaguardas}\nPerícias: {self.pericias}"