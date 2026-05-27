import pygame
import random 

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player vs. Enemies!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

enemy_colors = [RED, GREEN, BLUE, PURPLE, YELLOW]

player_size = 30
player_x = screen_width // 2 - player_size // 2 
player_y = screen_height - 50 
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
player_speed = 5
player_color = WHITE

enemy_size = 20
num_enemies = 7
enemies = [] 

def create_one_enemy():
    """Creates a new enemy with a random position and color."""
    ex = random.randint(0, screen_width - enemy_size) 
    ey = random.randint(0, screen_height // 2) 
    ecolor = random.choice(enemy_colors) 
    return {'rect': pygame.Rect(ex, ey, enemy_size, enemy_size), 'color': ecolor}

for _ in range(num_enemies):
    enemies.append(create_one_enemy())

score = 0
font = pygame.font.Font(None, 36) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_rect.x += player_speed
            if event.key == pygame.K_UP:
                player_rect.y -= player_speed
            if event.key == pygame.K_DOWN:
                player_rect.y += player_speed

    player_rect.x = max(0, min(player_rect.x, screen_width - player_size))
    player_rect.y = max(0, min(player_rect.y, screen_height - player_size))

    for i in range(len(enemies) - 1, -1, -1):
        enemy_data = enemies[i]
        if player_rect.colliderect(enemy_data['rect']):
            score += 1
            print(f"Score: {score}") 
            
         
            enemies.pop(i)
            enemies.append(create_one_enemy())

    screen.fill(BLACK) 

    pygame.draw.rect(screen, player_color, player_rect)

    for enemy_data in enemies:
        pygame.draw.rect(screen, enemy_data['color'], enemy_data['rect'])

    score_text = font.render(f"Score: {score}", True, WHITE) 
    screen.blit(score_text, (10, 10)) 

    pygame.display.flip() 

pygame.quit()