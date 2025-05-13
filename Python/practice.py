import pygame
import random
import sys

from project import PIXELS

pygame.init()

# Screen size
WIDTH = 650
HEIGHT = 650
BLOCK_SIZE = 25
PIXELS = 25
SQUARES = int(WIDTH / PIXELS)


# Colors

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

class Background:
   def draw(self, surface):
    surface.fill(BG1)
    counter = 0
    for row in range(SQUARES):
        for col in range(SQUARES):
            if counter % 2 == 0:
                pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
            if col != SQUARES - 1:
                counter += 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    color = active_color if x < mouse[0] < x+width and y < mouse[1] < y+height else inactive_color

    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, WHITE)
    text_rect = button_text.get_rect(center=(x + width//2, y + height//2))
    screen.blit(button_text, text_rect)

    if x < mouse[0] < x+width and y < mouse[1] < y+height:
        if click[0] == 1 and action:
            action()

def game():
    snake = [(100, 100)]
    direction = (BLOCK_SIZE, 0)
    apple = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))
    score = 0
    background = Background()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if head == apple:
            score += 1
            apple = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))
        else:
            snake.pop()

        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]
        ):
            break

        background.draw(screen)
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (*apple, BLOCK_SIZE, BLOCK_SIZE))
        show_score(score)
        pygame.display.update()
        clock.tick(10)

    game_over_screen()

def game_over_screen():
    while True:
        screen.fill(WHITE)
        message = font.render("Game Over!", True, RED)
        screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 3))

        draw_button("Retry", WIDTH // 2 - 60, HEIGHT // 2, 120, 50, GRAY, RED, game)
        draw_button("Quit", WIDTH // 2 - 60, HEIGHT // 2 + 70, 120, 50, GRAY, RED, quit_game)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def quit_game():
    pygame.quit()
    sys.exit()

game()
