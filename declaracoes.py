import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((950, 608))
#fonte para ser usada na UI
font = pygame.font.Font('freesansbold.ttf', 18)

#Campos:
fundo1 = pygame.image.load('imagens/campos/campo_nordeste.png')
fundo2 = pygame.image.load('imagens/campos/campo_brasileirao.png')
fundo3 = pygame.image.load('imagens/campos/campo 3.png')
fundo4 = pygame.image.load('imagens/campos/campo 4.png')

pygame.mixer.init(22050,-16,2,2048)
#sons
pygame.mixer.music.load('sons/hinosanta_fixed.wav')
pygame.mixer.music.play(-1)
son_playecomida = pygame.mixer.Sound('sons/Pickup_Coin4.wav')
son_upgrade = pygame.mixer.Sound('sons/Powerup10.wav')
son_morte = pygame.mixer.Sound('sons/Hit_Hurt6.wav')

cabeca_img = pygame.image.load('imagens/cobra/cabecacobra.png')
corpo_verm_img = pygame.image.load('imagens/cobra/c_corpo_verm.png')
corpo_preto_img = pygame.image.load('imagens/cobra/c_corpo_preto.png')
cauda_preto_img = pygame.image.load('imagens/cobra/c_cauda_preto.png')
cauda_verm_img = pygame.image.load('imagens/cobra/c_cauda_verm.png')
