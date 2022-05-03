import pygame, random
from pygame.locals import *

#IMAGENS IMPORT
fundo = pygame.image.load('campo.jpg')
SANTA = pygame.image.load('SANTA.png')
SPORTIMG = pygame.image.load('sport.png')
SALGUEIROIMG = pygame.image.load('SALGUEIRO.png')
cobracabeca = pygame.image.load('cabecacobra.png')
# Helper functions
#
def on_grid_random():
    x = random.randint(0,24)
    y = random.randint(0,18)
    return (x * 32, y * 32)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((800, 608))
pygame.display.set_caption('Cobra Coral')

snake = [(320, 320), (352, 320), (384,320)]
snake_skin = cobracabeca
# snake_skin = pygame.Surface((32,32))
# snake_skin.fill((255,0,255)) #White

apple_pos = on_grid_random()
apple = SANTA

sport_pos = on_grid_random()
SPORT = SPORTIMG

salgueiro_pos = on_grid_random()
salgueiro = SALGUEIROIMG

#apple.fill((255,0,0))

my_direction = RIGHT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], sport_pos):
        sport_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    if collision(snake[0], salgueiro_pos):
        salgueiro_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1

    # Check if snake collided with boundaries
    if snake[0][0] == 800 or snake[0][1] == 608 or snake[0][0] < 0 or snake[0][1] < 0:
        #son perdeu
        game_over = True
        break
    # Check if the snake has hit itself
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    # Actually make the snake move.
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 32)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 32)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 32, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 32, snake[0][1])
    
    screen.fill((0,100,0))
    screen.blit(fundo,(0,0))
    screen.blit(apple, apple_pos)
    screen.blit(SPORT, sport_pos)
    screen.blit(salgueiro, salgueiro_pos)

    

    for x in range(0, 800, 32): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 800))
    for y in range(0, 800, 32): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (800, y))

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (800 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 45)
    game_over_screen = game_over_font.render('Nautico foi para serie D', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (800 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()