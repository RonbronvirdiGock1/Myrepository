import random
import pygame

pygame.init()

screen_width = 800 
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Color-Changing Sprites")

GREY = (58, 58, 58)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

sprite_colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]

sprite1_size = 50
sprite1_x = 100
sprite1_y = 250
sprite1_rect = pygame.Rect(sprite1_x, sprite1_y, sprite1_size, sprite1_size)
sprite1_color = random.choice(sprite_colors) 
sprite1_speed = 5

sprite2_size = 50
sprite2_x = 650
sprite2_y = 250

sprite2_rect = pygame.Rect(sprite2_x, sprite2_y, sprite2_size, sprite2_size)
sprite2_color = random.choice(sprite_colors) 
sprite2_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                sprite1_rect.x -= sprite1_speed
                sprite1_color = random.choice(sprite_colors) 
            if event.key == pygame.K_RIGHT:
                sprite1_rect.x += sprite1_speed
                sprite1_color = random.choice(sprite_colors) 
            if event.key == pygame.K_UP:
                sprite1_rect.y -= sprite1_speed
                sprite1_color = random.choice(sprite_colors) 
            if event.key == pygame.K_DOWN:
                sprite1_rect.y += sprite1_speed
                sprite1_color = random.choice(sprite_colors)
           
            if event.key == pygame.K_a: 
                sprite2_rect.x -= sprite2_speed
                sprite2_color = random.choice(sprite_colors) 
            if event.key == pygame.K_d: 
                sprite2_rect.x += sprite2_speed
                sprite2_color = random.choice(sprite_colors) 
            if event.key == pygame.K_w: 
                sprite2_rect.y -= sprite2_speed
                sprite2_color = random.choice(sprite_colors) 
            if event.key == pygame.K_s: 
                sprite2_rect.y += sprite2_speed
                sprite2_color = random.choice(sprite_colors) 
   
    screen.fill(GREY) 
    
   
    pygame.draw.rect(screen, sprite1_color, sprite1_rect)
    
    
    pygame.draw.rect(screen, sprite2_color, sprite2_rect)

    pygame.display.flip() 

pygame.quit()