from re import A
from turtle import Screen
import pygame, random
from pygame.locals import *



#IMAGENS IMPORT
fundo1 = pygame.image.load('campo.jpg')
fundo2 = pygame.image.load('campo.png')
NAUTICOIMG = pygame.image.load('i_nautico.png')
SPORTIMG = pygame.image.load('i_sport.png')
SALGUEIROIMG = pygame.image.load('i_salgueiro.png')
cobracabeca = pygame.image.load('cabecacobra.png')
flamengoimg = pygame.image.load('i_flamengo.png')
corintiansimg = pygame.image.load('i_corintians.png')
japaoimg = pygame.image.load('i_japao.png')
jupterimg = pygame.image.load('i_jupiter.png')
marteimg = pygame.image.load('i_marte.png')
palmeirasimg = pygame.image.load('i_palmeiras.png')
saturnoimg = pygame.image.load('i_saturn.png')
alemanhaimg = pygame.image.load('i_alemanha.png')
argentinaimg = pygame.image.load('i_argentina.png')

#fundo variavel e fundo1 2 3 4 moveis
fundo = fundo1

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
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# variaveis que definem o numero para direcionar a cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#essa seção e a base do py games para inicar, criar uma janela e dar nome a janela
pygame.init()
screen = pygame.display.set_mode((950, 608))
pygame.display.set_caption('Cobra Coral')


#define nossa cobra em tamanho e skin
snake = [(320, 320), (352, 320), (384,320)]
# a skin tem que ser umaimagem 32x que vai ser o tanho real do objerto para a colisão funcianar corretamente
snake_head = cobracabeca
snake_corpo_verm = pygame.image.load('c_corpo_verm.png')
snake_corpo_preto = pygame.image.load('c_corpo_preto.png')
snake_cauda_verm = pygame.image.load('c_cauda_verm.png')
snake_cauda_preto = pygame.image.load('c_cauda_preto.png')

# snake_skin = pygame.Surface((32,32))
# snake_skin.fill((255,0,255)) #White

#define uma das "maçãs" que são um dos times
#primeiro é escohlido uma posiçao para a 'maçã' usando a função
P1_pos = on_grid_random()
# a skin tem que ser umaimagem 32x que vai ser o tanho real do objerto para a colisão funcianar corretamente
P1 = NAUTICOIMG
P1MOSTRADOR = NAUTICOIMG
# (Pergunta: pq foi criada uma variável cópia da img? não seria mais simples só usar a própria img dos times já que não vamos modificá-las) - Pedro

#define uma das "maçãs" que são um dos times
#primeiro é escohlido uma posiçao para a 'maçã' usando a função
P2_pos = on_grid_random()
# a skin tem que ser umaimagem 32x que vai ser o tanho real do objerto para a colisão funcianar corretamente
P2 = SPORTIMG
P2MOSTRADOR = SPORTIMG

#define uma das "maçãs" que são um dos times
#primeiro é escohlido uma posiçao para a 'maçã' usando a função
P3_pos = on_grid_random()
# a skin tem que ser umaimagem 32x que vai ser o tanho real do objerto para a colisão funcianar corretamente
P3 = SALGUEIROIMG
P3MOSTRADOR = SALGUEIROIMG

#esse codigo abaixo e quano um novo objeto ainda não recebeu cor
#apple.fill((255,0,0))

#indica o sentido inicial da cobrinha
my_direction = RIGHT

#diz que nosso jogo vai ser limitado pelo fps
clock = pygame.time.Clock()

#fonte para ser usada na UI
font = pygame.font.Font('freesansbold.ttf', 18)
#variavel score que mostra a pontuação
score = 0
#Variaveis que mostra a pontuaçõa individual de cada player
SCOREP1 = 0
SCOREP2 = 0
SCOREP3 = 0
scorenautico = 0
scoresporte = 0
scoresalgueiro = 0
scoreflamengo = 0 
scorecorintia = 0 
scorepalmeiras = 0
scorejapao = 0
scorealemanha = 0
scoreargentina = 0
scorejupter = 0
scoremarte = 0
scoresaturno = 0 

def pontuacao_na_tela(imagem, score_time, posicao):
    posicao = (5+posicao)*32
    screen.blit(imagem,(816,posicao))
    score_font = font.render('Score: %s' % (score_time), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (950 - 100, 6 + posicao)
    screen.blit(score_font, score_rect)

def pontuacao_estagio(SCOREPX, posicao):
    # atualiza o score, pega a fonte e atualiza na tela (para não ficar estatico)
    score_font = font.render('Score: %s' % (SCOREPX), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    #ajustar entre (950-120 a posiçao do texto)
    score_rect.topleft = (950 - 100, posicao)
    screen.blit(score_font, score_rect)

# variave responsavel para que o jogo nao feche apos um unico update
game_over = False
# esse while fica rodando grantido que o jogo continue rodando
while not game_over:
    #limitador do fps, colocamos aki o fps(tavz uma variavel funcione)-- porem se a variavel ficar almentando e diminuindo tem que colocar um limite max e min
    clock.tick(10)
    #esse for garante que que o jogo não feche enquanto não apertamos o X ou se apertamos o X ele vai fechar
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #esse conjuntos de evento recebem a informação de qual tecla esta apertada e redireciona a cobra 
        #sao eles up, down, left e rigth
        #IMPORTANTE!!!! O Player não pode ir na direção contraria 
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN: # se cima apertou e a cobra não esta indo pra baixo
                my_direction = UP
                snake_head = rotacao(cobracabeca, 90)
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                snake_head = rotacao(cobracabeca, -90)
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                snake_head = rotacao(cobracabeca, 180)
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                snake_head = rotacao(cobracabeca, 0)

    #TROCA DE IMG TESTE
    if score <= 15:
        scorenautico = SCOREP1
        scoresporte = SCOREP2
        scoresalgueiro = SCOREP3
    elif score > 15 and score <= 30:
        P1 = flamengoimg
        P2 = corintiansimg
        P3 = palmeirasimg
        P1MOSTRADOR = flamengoimg
        P2MOSTRADOR = corintiansimg
        P3MOSTRADOR = palmeirasimg
        scoreflamengo = SCOREP1
        scorecorintia = SCOREP2
        scorepalmeiras = SCOREP3
        fundo = fundo2
    elif score > 30 and score <= 45:
        P1 = japaoimg
        P2 = alemanhaimg
        P3 = argentinaimg
        P1MOSTRADOR = japaoimg
        P2MOSTRADOR = alemanhaimg
        P3MOSTRADOR = argentinaimg
        scorejapao = SCOREP1
        scorealemanha = SCOREP2
        scoreargentina = SCOREP3
        fundo = fundo1
    elif score > 45:
        P1 = jupterimg
        P2 = marteimg
        P3 = saturnoimg
        P1MOSTRADOR = jupterimg
        P2MOSTRADOR = marteimg
        P3MOSTRADOR = saturnoimg
        scorejupter = SCOREP1
        scoremarte = SCOREP2
        scoresaturno = SCOREP3
        fundo = fundo2

    if score == 15 :
        SCOREP1 = 0
        SCOREP2 = 0
        SCOREP3 = 0
    elif score == 30 :
        SCOREP1 = 0
        SCOREP2 = 0
        SCOREP3 = 0
    elif score == 45:
        SCOREP1 = 0
        SCOREP2 = 0
        SCOREP3 = 0


    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake[0], P1_pos): # -> snake[0] = coordenada do primeiro pedaço da cobra, que é a cabeça
        P1_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        SCOREP1 = SCOREP1 +1

    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake[0], P2_pos):
        P2_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        SCOREP2 = SCOREP2 +1

    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake[0], P3_pos):
        P3_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        SCOREP3 = SCOREP3 +1

    # Checa se a snake colidiu com a bordas
    if snake[0][0] == 800 or snake[0][1] == 608 or snake[0][0] < 0 or snake[0][1] < 0:
        #aki entra o son de perdeu
        game_over = True
        break
    # Checa se a cobra colidiu com ele mesma com um for
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            #aki entra o son de perdeu
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    # o codigo que de fato faz a cobra se mover
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 32) # -> snake[0] = (x, y)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 32)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 32, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 32, snake[0][1])
    
    #atualização da tela
    screen.fill((0,100,0))
    screen.blit(fundo,(0,0))
    screen.blit(P1, P1_pos)
    screen.blit(P2, P2_pos)
    screen.blit(P3, P3_pos)
    screen.blit(P1MOSTRADOR,(816,64))
    screen.blit(P2MOSTRADOR,(816,96))
    screen.blit(P3MOSTRADOR,(816,128))

    for i in range(1): # Essas funções vão apresentar a pontuação de um time especifico na tela
        pontuacao_na_tela(NAUTICOIMG, scorenautico, 1) # nautico é o mais em cima
        pontuacao_na_tela(SPORTIMG, scoresporte, 2) # sport vem depois
        pontuacao_na_tela(SALGUEIROIMG, scoresalgueiro, 3) # salgueiro é o 3o

        if score > 15:
            pontuacao_na_tela(flamengoimg, scoreflamengo, 4) # flamengo é o 4o
            pontuacao_na_tela(corintiansimg, scorecorintia, 5) # corinthians é o 5o
            pontuacao_na_tela(palmeirasimg, scorepalmeiras, 6) # palmeiras é o 6o

        if score > 30:
            pontuacao_na_tela(japaoimg, scorejapao, 7) # japao é o 7o
            pontuacao_na_tela(alemanhaimg, scorealemanha, 8) # alemanha é o 8o
            pontuacao_na_tela(argentinaimg, scoreargentina, 9) # argentina é o 9o

        if score > 45:
            pontuacao_na_tela(jupterimg, scorejupter, 10) # jupiter vem em 10o
            pontuacao_na_tela(marteimg, scoremarte, 11) # marte vem em 11o
            pontuacao_na_tela(saturnoimg, scoresaturno, 12) # e saturno é o último, em 12o de cima para baixo
    
    #marca (desenha) as linhas 
    for x in range(0, 800, 32): # horizontal lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 800))
    for y in range(0, 800, 32): # vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (800, y))

    # essas vão ser as pontuações específicas para os times dos estágios
    pontuacao_estagio(score, 10) # geral
    pontuacao_estagio(SCOREP1, 72) # time 1
    pontuacao_estagio(SCOREP2, 102) # time 2
    pontuacao_estagio(SCOREP3, 142) # time 3

    # atualiza a posição de cada pedaço da cobra na tela
    for pedaco in snake:
        #cabeça da cobra
        if snake.index(pedaco) == 0:
            screen.blit(snake_head, pedaco)
        #cauda da cobra
        elif snake.index(pedaco) == len(snake) - 1:
            #a cor da cauda muda de acordo com o tamanho da cobra
            if len(snake)%2 == 1:
                screen.blit(snake_cauda_preto, pedaco)
            else:
                screen.blit(snake_cauda_verm, pedaco)
        #corpo da cobra que recebe vermelho nas posições impares e preto nas pares (cabeça é 0)
        elif snake.index(pedaco)%2 != 0:
            screen.blit(snake_corpo_verm, pedaco)
        else:
            screen.blit(snake_corpo_preto, pedaco)

    #comando mais importante o de update da tele, garante que ao final do grande while e vonsiga mostrar tudo que aconteu na tela
    pygame.display.update()

# quando aquele while acabar vaintar eternamente nesse while de game over
while True:
    #define uma fonte para o texto de game over, local de spw, oq vai ser escrito, e tempo de espera ate a tela fechar
    game_over_font = pygame.font.Font('freesansbold.ttf', 45)
    game_over_screen = game_over_font.render('Santinha foi para serie D', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (800 / 2, 100)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
