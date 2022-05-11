from declaracoes import *

# Times
class time(object):
    def __init__(self, imagem):
        self.brasao = imagem  
        self.pontos = 0

    def adicionar_um(self):
        self.pontos += 1

    def pontuacao_na_tela(self, posicao):
        posicao = (5+posicao)*32
        screen.blit(self.brasao,(816,posicao))
        score_font = font.render('Score: %s' % (self.pontos), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (950 - 100, 6 + posicao)
        screen.blit(score_font, score_rect)

nautico = time(pygame.image.load('imagens/times/i_nautico.png'))
sport = time(pygame.image.load('imagens/times/i_sport.png'))
salgueiro = time(pygame.image.load('imagens/times/i_salgueiro.png'))
flamengo = time(pygame.image.load('imagens/times/i_flamengo.png'))
corinthians = time(pygame.image.load('imagens/times/i_corintians.png'))
palmeiras = time(pygame.image.load('imagens/times/i_palmeiras.png'))
japao = time(pygame.image.load('imagens/times/i_japao.png'))
alemanha = time(pygame.image.load('imagens/times/i_alemanha.png'))
argentina = time(pygame.image.load('imagens/times/i_argentina.png'))
marte = time(pygame.image.load('imagens/times/i_marte.png'))
jupiter = time(pygame.image.load('imagens/times/i_jupiter.png'))
saturno = time(pygame.image.load('imagens/times/i_saturn.png'))

# Pedaços da cobra
class Cobra(object):
    def __init__(self, x, y, imagem):
        #define nossa cobra em tamanho e skin
        self.posicaoX = x 
        self.posicaoY = y 
        self.posicao = (self.posicaoX, self.posicaoY)
        self.sprite = imagem 

    def update_pos(self, new_x, new_y):
        self.posicaoX = new_x
        self.posicaoY = new_y
        self.posicao = (self.posicaoX, self.posicaoY)

    def update_sprite(self, new_imagem):
        self.sprite = new_imagem 

    def rotacao(self, angulo):
        sprite_rodado = pygame.transform.rotate(self.sprite, angulo)
        return sprite_rodado

cabeca = Cobra(320, 320, cabeca_img)
corpo1 = Cobra(352, 320, corpo_verm_img)
cauda = Cobra(384, 320, cauda_preto_img)
