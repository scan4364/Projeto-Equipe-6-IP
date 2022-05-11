# from re import A
# from turtle import Screen
import pygame, random
from pygame.locals import *
from classes import *
from funcoes import *

pygame.display.set_caption('Santa Ascends')

snake = Cobra()
snake_head = snake.cabeca

#IMAGENS IMPORT
#telas
start_img = pygame.image.load('imagens/telas/santa_ascends950.png')
dead_img = pygame.image.load('imagens/telas/santa_dies_950.png')
creditos_img = pygame.image.load('imagens/telas/santa_creditos.png')

#tocou é variuaveis bool que impede que o som repita infiniramente
tocou1 = False
tocou2 = False
tocou3 = False

#fundo variavel e fundo1 2 3 4 moveis
fundo = fundo1

# variaveis que definem o numero para direcionar a cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#define cada uma das "maçãs" que são um dos times
#primeiro é escolhido uma posiçao para a 'maçã' usando a função
time1_pos = on_grid_random()
time2_pos = on_grid_random()
time3_pos = on_grid_random()
# a skin tem que ser umaimagem 32x que vai ser o tanho real do objerto para a colisão funcianar corretamente
time1 = nautico
time2 = sport
time3 = salgueiro 

#indica o sentido inicial da cobrinha
my_direction = RIGHT

#diz que nosso jogo vai ser limitado pelo fps
clock = pygame.time.Clock()

#variavel score que mostra a pontuação
score = 0

play_game = False
while not play_game:
    #esse for garante que que o jogo não feche enquanto não apertamos o X ou se apertamos o X ele vai fechar
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    clock.tick(10)
    screen.fill((0,100,0))
    screen.blit(start_img,(0,0))

    game_star_font3 = pygame.font.Font('freesansbold.ttf', 15)
    game_star_screen3 = game_star_font3.render('Click na tela para Jogar!', True, (255, 255, 255))
    game_star_rect3 = game_star_screen3.get_rect()
    game_star_rect3.midtop = (950 / 2, 550)
    screen.blit(game_star_screen3, game_star_rect3)

    pressed_Keys = pygame.mouse.get_pressed()
    if (pressed_Keys[0]):
        play_game = True

    pygame.display.update()

# variavel responsavel para que o jogo nao feche apos um unico update
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
                pygame.transform.rotate(snake.cabeca, 90)
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                pygame.transform.rotate(snake.cabeca, -90)
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                pygame.transform.rotate(snake.cabeca, 180)
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                pygame.transform.rotate(snake.cabeca, 0)

    #TROCA DE IMG TESTE
    if score < 15:
        time1 = nautico
        time2 = sport
        time3 = salgueiro
        fundo = fundo1
    elif score >= 15 and score < 30:
        time1 = flamengo 
        time2 = corinthians
        time3 = palmeiras 
        fundo = fundo2
        if(score == 15 and not tocou1):
            son_upgrade.play()
            tocou1 = True
    elif score >= 30 and score < 45:
        time1 = japao
        time2 = alemanha 
        time3 = argentina 
        fundo = fundo3
        if(score == 30 and not tocou2):
            son_upgrade.play()
            tocou2 = True
    elif score >= 45:
        time1 = marte 
        time2 = jupiter
        time3 = saturno 
        fundo = fundo4
        if(score == 45 and not tocou3):
            son_upgrade.play()
            tocou3 = True

    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake.corpo[0], time1_pos): # -> snake.corpo[0] = coordenada do primeiro pedaço da cobra, que é a cabeça
        time1_pos = on_grid_random()
        snake.corpo.append((0,0))
        score += 1 
        time1.adicionar_um()
        son_playecomida.play()

    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake.corpo[0], time2_pos):
        time2_pos = on_grid_random()
        snake.corpo.append((0,0))
        score += 1
        time2.adicionar_um()
        son_playecomida.play()

    #esse bloco de comando detecta se a colisao com a 'maçã' e adiciona uma nova parte onde era a 'maçã' e redireciona a 'maçã' para umanova posiçao e adiciona a pontuaçao 1
    if collision(snake.corpo[0], time3_pos):
        time3_pos = on_grid_random()
        snake.corpo.append((0,0))
        score += 1
        time3.adicionar_um()
        son_playecomida.play()

    # Checa se a snake.corpo colidiu com a bordas
    if snake.corpo[0][0] == 800 or snake.corpo[0][1] == 608 or snake.corpo[0][0] < 0 or snake.corpo[0][1] < 0:
        #aki entra o son de perdeu
        son_morte.play()
        game_over = True
        break
    # Checa se a cobra colidiu com ele mesma com um for
    for i in range(1, len(snake.corpo) - 1):
        if snake.corpo[0][0] == snake.corpo[i][0] and snake.corpo[0][1] == snake.corpo[i][1]:
            son_morte.play()
            game_over = True
            #aki entra o son de perdeu
            break

    if game_over:
        son_morte.play()
        break
    
    for i in range(len(snake.corpo) - 1, 0, -1):
        snake.corpo[i] = (snake.corpo[i-1][0], snake.corpo[i-1][1])
        
    # o codigo que de fato faz a cobra se mover
    if my_direction == UP:
        snake.corpo[0] = (snake.corpo[0][0], snake.corpo[0][1] - 32) # -> snake.corpo[0] = (x, y)
    if my_direction == DOWN:
        snake.corpo[0] = (snake.corpo[0][0], snake.corpo[0][1] + 32)
    if my_direction == RIGHT:
        snake.corpo[0] = (snake.corpo[0][0] + 32, snake.corpo[0][1])
    if my_direction == LEFT:
        snake.corpo[0] = (snake.corpo[0][0] - 32, snake.corpo[0][1])
    
    #atualização da tela
    screen.fill((0,100,0))
    screen.blit(fundo,(0,0))
    screen.blit(time1.brasao, time1_pos)
    screen.blit(time2.brasao, time2_pos)
    screen.blit(time3.brasao, time3_pos)
    screen.blit(time1.brasao,(816,64))
    screen.blit(time2.brasao,(816,96))
    screen.blit(time3.brasao,(816,128))

    for i in range(1):
        nautico.pontuacao_na_tela(1) # nautico é o mais em cima
        sport.pontuacao_na_tela(2) # sport vem depois
        salgueiro.pontuacao_na_tela(3) # salgueiro é o 3o

        if score >= 15:
            flamengo.pontuacao_na_tela(4) # flamengo é o 4o
            corinthians.pontuacao_na_tela(5) # corinthians é o 5o
            palmeiras.pontuacao_na_tela(6) # palmeiras é o 6o

        if score >= 30:
            japao.pontuacao_na_tela(7) # japao é o 7o
            alemanha.pontuacao_na_tela(8) # alemanha é o 8o
            argentina.pontuacao_na_tela(9) # argentina é o 9o

        if score >= 45:
            jupiter.pontuacao_na_tela(10) # jupiter vem em 10o
            marte.pontuacao_na_tela(11) # marte vem em 11o
            saturno.pontuacao_na_tela(12) # e saturno é o último, em 12o de cima para baixo

    #marca (desenha) as linhas 
    for x in range(0, 800, 32): # horizontal lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 800))
    for y in range(0, 800, 32): # vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (800, y))


    # essas vão ser as pontuações específicas para os times dos estágios
    pontuacao_estagio(score, 10) # geral
    pontuacao_estagio(time1.pontos, 72) # time 1
    pontuacao_estagio(time2.pontos, 102) # time 2
    pontuacao_estagio(time3.pontos, 142) # time 3

    # atualiza a posiçãode cada pedaço da cobra na tela
    for pedaco in snake.corpo:
    #cabeça da cobra
        if snake.corpo.index(pedaco) == 0:
            screen.blit(snake_head, pedaco)
        #cauda da cobra tamanho
        elif snake.corpo.index(pedaco) == len(snake.corpo) - 1:
            #a cor da cauda muda de acordo com o tamanho da cobra
            if len(snake.corpo)%2 == 1:
                screen.blit(snake.cauda_preto, pedaco)
            else:
                screen.blit(snake.cauda_verm, pedaco)
    #corpo da cobra que recebe vermelho nas posições impares e preto nas pares (cabeça é 0)
        elif snake.corpo.index(pedaco)%2 != 0:
            screen.blit(snake.corpo_verm, pedaco)
        else:
            screen.blit(snake.corpo_preto, pedaco) 

    #comando mais importante o de update da tele, garante que ao final do grande while e vonsiga mostrar tudo que aconteu na tela
    pygame.display.update()

game_over_bl = True
while game_over_bl == True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    clock.tick(10)
    screen.fill((0,100,0))
    screen.blit(dead_img,(0,0))
    game_over_font = pygame.font.Font('freesansbold.ttf', 35)
    game_over_screen = game_over_font.render('Santinha foi para a série D', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (950 / 2, 500)
    screen.blit(game_over_screen, game_over_rect)

    game_next_font2 = pygame.font.Font('freesansbold.ttf', 15)
    game_next_screen2 = game_next_font2.render('Click na tela para abrir os créditos', True, (255, 255, 255))
    game_next_rect2 = game_next_screen2.get_rect()
    game_next_rect2.midtop = (950 / 2, 550)
    screen.blit(game_next_screen2, game_next_rect2)

    pressed_Keys = pygame.mouse.get_pressed()
    if (pressed_Keys[0]):
        game_over_bl = False

    pygame.display.update()

creditos_bl = True
while creditos_bl:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    clock.tick(10)
    screen.fill((0,100,0))
    screen.blit(creditos_img,(0,0))

    game_over_font2 = pygame.font.Font('freesansbold.ttf', 15)
    game_over_screen2 = game_over_font2.render('Click na tela para fechar o jogo', True, (255, 255, 255))
    game_over_rect2 = game_over_screen2.get_rect()
    game_over_rect2.midtop = (950 / 2, 550)
    screen.blit(game_over_screen2, game_over_rect2)
    
    pressed_Keys = pygame.mouse.get_pressed()
    if (pressed_Keys[0]):
        creditos_bl = False

    pygame.display.update()

