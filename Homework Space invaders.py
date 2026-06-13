import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_SPEED = 5
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40

BULLET_SPEED = 10
NUM_ENEMIES = 6
FPS = 60

PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

# Background Music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Sound Effects
laser_sound = pygame.mixer.Sound("laser.mp3")
explosion_sound = pygame.mixer.Sound("explosion.mp3")

# Images
background = pygame.image.load("Background 2.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_img = pygame.image.load("Rocket 1.png")
player_img = pygame.transform.scale(player_img, (64, 64))

enemy_img = pygame.image.load("enemy 1.png")
enemy_img = pygame.transform.scale(enemy_img, (64, 64))

bullet_img = pygame.image.load("bullet_1.png")
bullet_img = pygame.transform.scale(bullet_img, (32, 32))

# Fonts
font = pygame.font.Font("freesansbold.ttf", 32)
game_over_font = pygame.font.Font("freesansbold.ttf", 64)

def reset_game():
    global player_x
    global player_y
    global player_x_change
    global bullet_x
    global bullet_y
    global bullet_state
    global score
    global game_over

    player_x = PLAYER_START_X
    player_y = PLAYER_START_Y
    player_x_change = 0

    bullet_x = 0
    bullet_y = player_y
    bullet_state = "ready"

    score = 0
    game_over = False

    enemies.clear()

    for _ in range(NUM_ENEMIES):
        enemies.append({
            "x": random.randint(0, SCREEN_WIDTH - 64),
            "y": random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX),
            "dx": ENEMY_SPEED_X
        })

def show_score():
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

def show_game_over():
    text = game_over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    restart = font.render(
        "Press R to Restart",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (190, 180))
    screen.blit(restart, (240, 260))

def draw_player():
    screen.blit(player_img, (player_x, player_y))

def draw_enemy(enemy):
    screen.blit(enemy_img, (enemy["x"], enemy["y"]))

def fire_bullet():
    screen.blit(
        bullet_img,
        (bullet_x + 16, bullet_y + 10)
    )

enemies = []
reset_game()

running = True

while running:

    clock.tick(FPS)

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x_change = -PLAYER_SPEED

            if event.key == pygame.K_RIGHT:
                player_x_change = PLAYER_SPEED

            if not game_over:

                if event.key == pygame.K_SPACE and bullet_state == "ready":

                    laser_sound.play()

                    bullet_x = player_x
                    bullet_y = player_y
                    bullet_state = "fire"

            if game_over and event.key == pygame.K_r:
                reset_game()

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    if not game_over:

        player_x += player_x_change

        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - 64:
            player_x = SCREEN_WIDTH - 64

        if bullet_state == "fire":

            bullet_y -= BULLET_SPEED

            if bullet_y < 0:
                bullet_state = "ready"

        for enemy in enemies:

            enemy["x"] += enemy["dx"]

            if enemy["x"] <= 0:
                enemy["dx"] = ENEMY_SPEED_X
                enemy["y"] += ENEMY_SPEED_Y

            elif enemy["x"] >= SCREEN_WIDTH - 64:
                enemy["dx"] = -ENEMY_SPEED_X
                enemy["y"] += ENEMY_SPEED_Y

            if enemy["y"] > 340:
                game_over = True

            if bullet_state == "fire":

                enemy_rect = enemy_img.get_rect(
                    topleft=(enemy["x"], enemy["y"])
                )

                bullet_rect = bullet_img.get_rect(
                    topleft=(bullet_x + 16, bullet_y + 10)
                )

                if enemy_rect.colliderect(bullet_rect):

                    explosion_sound.play()

                    bullet_state = "ready"
                    bullet_y = player_y

                    score += 1

                    enemy["x"] = random.randint(
                        0,
                        SCREEN_WIDTH - 64
                    )

                    enemy["y"] = random.randint(
                        ENEMY_START_Y_MIN,
                        ENEMY_START_Y_MAX
                    )

    draw_player()

    for enemy in enemies:
        draw_enemy(enemy)

    if bullet_state == "fire":
        fire_bullet()

    show_score()

    if game_over:
        show_game_over()

    pygame.display.update()

pygame.quit()