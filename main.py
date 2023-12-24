import pygame
from pygame.locals import QUIT
from sys import exit
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
    personagem2 = personagem("Personagem 2")
    
    mostrar_personagens()
    
    
    
    
    
    
def mostrar_personagens():
    for i in personagem.lista_personagens:
        print(i)
        print("=========================================")
    
if __name__ == "__main__":
    main()
    
        