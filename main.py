import pygame
import sys
import character
import screen

# Initialize Pygame
pygame.init()

# Set up the display
# screen_width = 800
# screen.screen_height = 600
screen_var = pygame.display.set_mode((screen.screen_width, screen.screen_height))
pygame.display.set_caption("Simple Platformer")

# # Character variables
# character.character_width = 50
# character.character_height = 50
# character.character_x = screen_width // 2 - character.character_width // 2
# character.character.character_y = screen.screen_height - character.character_height
# character_color = (255, 0, 0)  # Red
# 
# character_speed = 5


# Platform variables
platform_width = 200
platform_height = 20
platform_x = screen.screen_width // 2 - platform_width // 2
platform_y = screen.screen_height - 100
platform_color = (0, 255, 0)  # Green

# Jump variables
is_jumping = False
jump_speed = 10
gravity = 0.5
vertical_velocity = 0


# Collision detection function
def check_collision(x, y, width, height, plat_x, plat_y, plat_width, plat_height):
    if x < plat_x + plat_width and x + width > plat_x and y < plat_y + plat_height and y + height > plat_y:
        return True
    return False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Jump event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                vertical_velocity = -jump_speed

    # Check for pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.character_x -= character.character_speed
    if keys[pygame.K_RIGHT]:
        character.character_x += character.character_speed

    # Jumping logic
    if is_jumping:
        character.character_y += vertical_velocity
        vertical_velocity += gravity
        if character.character_y >= screen.screen_height - character.character_height:
            character.character_y = screen.screen_height - character.character_height
            is_jumping = False

    # Jumping and gravity logic
    if is_jumping:
        character.character_y += vertical_velocity
        vertical_velocity += gravity

        # Check for ground collision
        if character.character_y >= screen.screen_height - character.character_height:
            character.character_y = screen.screen_height - character.character_height
            is_jumping = False

        # Check for platform collision
        if check_collision(character.character_x, character.character_y, character.character_width, character.character_height, platform_x, platform_y, platform_width, platform_height):
            character.character_y = platform_y - character.character_height
            is_jumping = False

    # Fill the screen with a color (e.g., blue)
    screen_var.fill((0, 105, 148))

    # Draw the character
    pygame.draw.rect(screen_var, character.character_color, (character.character_x, character.character_y, character.character_width, character.character_height))

    # Draw the platform
    pygame.draw.rect(screen_var, platform_color, (platform_x, platform_y, platform_width, platform_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
