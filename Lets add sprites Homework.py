import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Snowman Game with a Tree!")

BLUE = (173, 216, 230)  
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)      
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
DARK_GREEN = (34, 139, 34)

snowman_top_x = screen_width // 2
snowman_top_y = screen_height - 100 - 30
snowman_speed = 5

hat_width = 60
hat_height = 40
hat_brim_height = 10

tree_trunk_width = 30
tree_trunk_height = 100
tree_x = 150 
tree_y = screen_height - tree_trunk_height - 20 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snowman_top_x -= snowman_speed
            if event.key == pygame.K_RIGHT:
                snowman_top_x += snowman_speed
            if event.key == pygame.K_UP:
                snowman_top_y -= snowman_speed
            if event.key == pygame.K_DOWN:
                snowman_top_y += snowman_speed

    if snowman_top_x < 0 + 20: snowman_top_x = 0 + 20
    if snowman_top_x > screen_width - 20: snowman_top_x = screen_width - 20
    if snowman_top_y < 0 + 20: snowman_top_y = 0 + 20
    if snowman_top_y > screen_height - 20: snowman_top_y = screen_height - 20

    screen.fill(BLUE)

    pygame.draw.rect(screen, BROWN, (tree_x, tree_y, tree_trunk_width, tree_trunk_height))
    
    pygame.draw.polygon(screen, DARK_GREEN, [
        (tree_x + tree_trunk_width // 2, tree_y),
        (tree_x - 20, tree_y + 50),
        (tree_x + tree_trunk_width + 20, tree_y + 50) 
    ])
    pygame.draw.polygon(screen, DARK_GREEN, [
        (tree_x + tree_trunk_width // 2, tree_y + 30), 
        (tree_x - 25, tree_y + 80),
        (tree_x + tree_trunk_width + 25, tree_y + 80)
    ])

    pygame.draw.circle(screen, WHITE, (snowman_top_x, snowman_top_y + 80), 40)
    pygame.draw.circle(screen, WHITE, (snowman_top_x, snowman_top_y + 30), 30)
    pygame.draw.circle(screen, WHITE, (snowman_top_x, snowman_top_y - 20), 20)

    pygame.draw.circle(screen, BLACK, (snowman_top_x - 8, snowman_top_y - 25), 3)
    pygame.draw.circle(screen, BLACK, (snowman_top_x + 8, snowman_top_y - 25), 3)

    nose_points = [(snowman_top_x, snowman_top_y - 20), (snowman_top_x - 5, snowman_top_y - 15), (snowman_top_x + 5, snowman_top_y - 15)]
    pygame.draw.polygon(screen, ORANGE, nose_points)

    hat_top_rect = pygame.Rect(snowman_top_x - hat_width // 2, snowman_top_y - 60, hat_width, hat_height)
    pygame.draw.rect(screen, BLACK, hat_top_rect)
    hat_brim_rect = pygame.Rect(snowman_top_x - (hat_width // 2 + 5), snowman_top_y - 60 + hat_height - 5, hat_width + 10, hat_brim_height)
    pygame.draw.rect(screen, BLACK, hat_brim_rect)

    pygame.display.flip() 

pygame.quit()