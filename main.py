import pygame
from pygame.locals import QUIT
from sys import exit
from classes.bases.habilidades import habilidades
from classes.personagens import personagem

LARGURA = 640
ALTURA = 480
        
def main():
    #pygame.init()
    #tela = pygame.display.set_mode((LARGURA, ALTURA))
    #pygame.display.set_caption('Dungeons & Pythons')
    #while True:
    #    
    #    
    #    for event in pygame.event.get():
    #        if event.type == QUIT:
    #            pygame.quit()
    #            exit()
    #    pygame.display.update()
    
    personagem1 = personagem("Personagem 1")
    personagem1.hp.set_hp(20)
    personagem1.hp.set_hp_temp(5)
    personagem1.hp.set_dados_vida(1, 8)
    
    atributos_base = {
        "Força": [12, 0],
        "Destreza": [13, 0],
        "Constituição": [9, 0],
        "Inteligência": [12, 0],
        "Sabedoria": [18, 0],
        "Carisma": [7, 0]
    }
    
    salvaguardas = {
        "Força": True,
        "Destreza": False,
        "Constituição": True,
        "Inteligência": False,
        "Sabedoria": False,
        "Carisma": True
    }
    
    pericias = {
        "Acrobacia": ["Destreza", False],
        "Arcanismo": ["Inteligência", False],
        "Atletismo": ["Força", True],
        "Atuação": ["Carisma", False],
        "Enganação": ["Carisma", False],
        "Furtividade": ["Destreza", False],
        "História": ["Inteligência", True],
        "Intimidação": ["Carisma", False],
        "Intuição": ["Sabedoria", False],
        "Investigação": ["Inteligência", False],
        "Lidar com Animais": ["Sabedoria", False],
        "Medicina": ["Sabedoria", False],
        "Natureza": ["Inteligência", True],
        "Percepção": ["Sabedoria", False],
        "Persuasão": ["Carisma", True],
        "Prestidigitação": ["Destreza", True],
        "Religião": ["Inteligência", False],
        "Sobrevivência": ["Sabedoria", False]
    }
    
    personagem1.set_habilidades(habilidades(atributos_base, 2, salvaguardas, pericias))
    
    #personagem2 = personagem("Personagem 2")
    
    #mostrar_personagens()
    modificador1 = personagem1.get_modificador_salvaguarda("Força")
    modificador2 = personagem1.get_modificador_salvaguarda("Destreza")
    modificador3 = personagem1.get_modificador_pericia("Atletismo")
    modificador4 = personagem1.get_modificador_pericia("História")
    
    print("Hp:\t\t", personagem1.hp)
    print("Força:\t\t", modificador1)
    print("Destreza:\t", modificador2)
    print("Atletismo:\t", modificador3)
    print("História:\t", modificador4)
    print("=========================================")
    
    personagem1.hp.dano(10)
    personagem1.habilidades_temp.set_proficiencia(4)
    
    modificador1 = personagem1.get_modificador_salvaguarda("Força")
    modificador2 = personagem1.get_modificador_salvaguarda("Destreza")
    modificador3 = personagem1.get_modificador_pericia("Atletismo")
    modificador4 = personagem1.get_modificador_pericia("História")
    
    print("Hp:\t\t", personagem1.hp)
    print("Força:\t\t", modificador1)
    print("Destreza:\t", modificador2)
    print("Atletismo:\t", modificador3)
    print("História:\t", modificador4)
    print("=========================================")
    
def mostrar_personagens():
    for i in personagem.lista_personagens:
        print(i)
        print("=========================================")
    
    
if __name__ == "__main__":
    main()
    

    
        