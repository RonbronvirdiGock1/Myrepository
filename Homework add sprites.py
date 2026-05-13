import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle Sprites")

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 80, 80)

clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 60, 60)

enemy = pygame.Rect(500, 300, 80, 80)

speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()