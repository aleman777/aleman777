import pygame
import random
import sys

GAME_WIDTH = 600
GAME_HEIGHT = 400
PIXELS = 40
SQUARES = int(GAME_WIDTH / PIXELS)
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)

#colors
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

class Background:
    def draw(self, surface):
      surface.fill( BG1 )
    counter = 0



pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

background = Background()



def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    color = active_color if x < mouse[0] < x + width and y < mouse[1] < y + height else inactive_color
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = font.render(text, True, WHITE)
    text_rect = button_text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(button_text, text_rect)

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if click[0] == 1 and action:
            action()


def game_over_screen():
    while True:
        screen.fill(BLACK)
        message = font.render("GAME OVER!", True, RED)
        screen.blit(message, (GAME_WIDTH // 2 - message.get_width() // 2, GAME_HEIGHT // 3))
        draw_button("Retry", GAME_WIDTH // 2 - 60, GAME_HEIGHT // 2 - 150, 120, 50, GRAY, RED, game)
        draw_button("Quit", GAME_WIDTH // 2 - 60, GAME_HEIGHT // 2 + 70, 120, 50, GRAY, RED, quit_game)
        pygame.display.update()


def quit_game():
    pygame.quit()
    sys.exit()


def game():
    snake = [(100, 100)]
    direction = (BLOCK_SIZE, 0)
    apple = (random.randrange(0, GAME_WIDTH, BLOCK_SIZE), random.randrange(0, GAME_HEIGHT, BLOCK_SIZE))
    score = 0

    while True:
        background.draw(screen)

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
            apple = (random.randrange(0, GAME_WIDTH, BLOCK_SIZE), random.randrange(0, GAME_HEIGHT, BLOCK_SIZE))
        else:
            snake.pop()

        if (
            head[0] < 0 or head[0] >= GAME_WIDTH or
            head[1] < 0 or head[1] >= GAME_HEIGHT or
            head in snake[1:]
        ):
            game_over_screen()

       # screen.fill(BLACK)
        for segment in snake:
            pygame.draw.rect(screen, BLUE, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (*apple, BLOCK_SIZE, BLOCK_SIZE))
        show_score(score)
        pygame.display.update()

        clock.tick(15)


if __name__ == "__main__":
    game()







