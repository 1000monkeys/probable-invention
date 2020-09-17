import sys
import random
import pygame
from pygame.sprite import Group
from star import Star


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Stars")

    star_image = pygame.image.load("star.png")
    star_rect = star_image.get_rect()
    stars = Group()

    available_space_x = 1024
    number_stars_x = int(available_space_x / (star_rect.width * 2))

    available_space_y = 768
    number_stars_y = int(available_space_y / (star_rect.height * 2))

    print(str(number_stars_x) + " = x && y = " + str(number_stars_y))

    # Fill stars
    for x in range(number_stars_x):
        for y in range(number_stars_y):
            star = Star(screen, star_image)
            star.rect.x = x * (star_rect.width * 2) + random.randint(-10, 10)
            star.rect.y = y * (star_rect.height * 2) + random.randint(-10, 10)
            stars.add(star)

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Watch for keyboard and mouse events.
        screen.fill((0, 0, 0))

        # Render all stars
        for star in stars:
            star.blitme()

        # Redraw the screen during each pass through the loop
        pygame.display.flip()


run_game()
