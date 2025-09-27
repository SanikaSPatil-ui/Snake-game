import pygame, random, sys
pygame.init()

# Game constants
SIZE = 20
WIDTH = 400
HEIGHT = 400

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK, GREEN, RED = (0, 0, 0), (0, 200, 0), (200, 0, 0)

# Snake setup
snake = [(100, 100)]
dx, dy = SIZE, 0  # moving right by default
food = (200, 200)

while True:
    # Event handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -SIZE
            if e.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, SIZE
            if e.key == pygame.K_LEFT and dx == 0:
                dx, dy = -SIZE, 0
            if e.key == pygame.K_RIGHT and dx == 0:
                dx, dy = SIZE, 0

    # MOVE SNAKE
    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    # Check food
    if head == food:
        food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))
    else:
        snake.pop()

    # Collision check
    if (head in snake[1:] or not 0 <= head[0] < WIDTH or not 0 <= head[1] < HEIGHT):
        print('Game Over! Your score was:', len(snake)-1)
        pygame.quit()
        sys.exit()

    # DRAW
    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, SIZE-1, SIZE-1))
    pygame.draw.rect(screen, RED, (food[0], food[1], SIZE-1, SIZE-1))  # draw food
    pygame.display.flip()
    clock.tick(10)
