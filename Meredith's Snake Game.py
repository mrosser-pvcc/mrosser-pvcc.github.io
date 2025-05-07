import pygame
import sys
import random

pygame.init()

SW, SH = 500, 500

BLOCK_SIZE = 25
font = pygame.font.SysFont('comicsans', 25)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('♦ Snake ♦')
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
        if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
            self.dead = True

        if self.dead:
            return

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "#f6f77a",self.rect)

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#7b577d", rect, 1)

def show_game_over_screen(screen, font, score_value):
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    score_text = font.render(f"Score: {score_value}", True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (150, 150))
        screen.blit(score_text, (180, 190))
        screen.blit(restart_text, (60, 230))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return

score = font.render("1", True, (255, 255, 255))
score_rect = score.get_rect(center=(SW/20, SH/20))

drawGrid()

snake = Snake()

apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_w:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_s:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
            elif event.key == pygame.K_a:
                snake.ydir = 0
                snake.xdir = -1
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_d:
                snake.ydir = 0
                snake.xdir = 1

    snake.update()

    screen.fill((0, 0, 0))
    drawGrid()

    apple.update()

    score = font.render(f"{len(snake.body) + 1}", True, (255, 255, 255))

    pygame.draw.rect(screen, "#a2feff", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "#a2feff", square)

    screen.blit(score, score_rect)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    if snake.dead:
        show_game_over_screen(screen, font, len(snake.body) + 1)
        snake = Snake()
        apple = Apple()
        continue

    pygame.draw.rect(screen, (0, 255, 0), snake.head)
    for segment in snake.body:
        pygame.draw.rect(screen, (0, 200, 0), segment)

    pygame.display.update()
    clock.tick(10)
