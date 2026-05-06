import pygame

pygame.init()
pygame.font.init() # Initialize the font module here!

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen") # This is still for the window's title bar

grey = (58, 58, 58)

cricket_image = pygame.image.load("image.png")
cricket_image = pygame.transform.scale(cricket_image, (300, 300))
image_rect = cricket_image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# --- New code for text below the image ---
# 1. Choose a font and size
font = pygame.font.Font(None, 36) # None for default font, 36 is the size
# 2. Render the text (turn it into an image)
text_surface = font.render("My First Game Screen", True, (255, 255, 255)) # White color
# 3. Get its rectangle to position it
text_rect = text_surface.get_rect()
# 4. Position it below the image
text_rect.centerx = screen_width // 2 # Center it horizontally
text_rect.top = image_rect.bottom + 10 # Place it 10 pixels below the image
# --- End new code ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    screen.blit(cricket_image, image_rect)
    screen.blit(text_surface, text_rect) # Draw the text onto the screen!

    pygame.display.flip()

pygame.quit()