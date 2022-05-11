import random
from declaracoes import *
from classes import *

# Helper functions
# função que escolhe um lugar aleatoria para o spw dos times 
def on_grid_random():
    x = random.randint(0,24)
    y = random.randint(0,18)
    return (x * 32, y * 32)

# função para girar a cabeça da cobra
def rotacao(img, angulo):
    img_rotacionada = pygame.transform.rotate(img, angulo)
    return img_rotacionada

#função que analisa se ha colisaão de objetos
#def colisao(cobra_lista: list):
#    novo_pedaco = Cobra(-32, -32, novo_sprite(cobra_lista[-1]))
#    cobra_lista.insert(-1, novo_pedaco)
#    cobra_lista[-1].sprite = nova_cor(cobra_lista[-1])
#    score += 1 
#    son_playecomida.play()

def nova_cor(rabo):
    if(rabo.sprite == cauda_preto_img):
        return cauda_verm_img
    elif(rabo.sprite == cauda_verm_img):
        return cauda_preto_img

def novo_sprite(rabo):
    if(rabo.sprite == cauda_preto_img):
        sprite = corpo_preto_img
    elif(rabo.sprite == cauda_verm_img):
        sprite = corpo_verm_img
    return sprite

def pontuacao_estagio(SCOREPX, posicao):
    # atualiza o score, pega a fonte e atualiza na tela (para não ficar estatico)
    score_font = font.render('Score: %s' % (SCOREPX), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    #ajustar entre (950-120 a posiçao do texto)
    score_rect.topleft = (950 - 100, posicao)
    screen.blit(score_font, score_rect)