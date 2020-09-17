import sys
import random
import pygame
from pygame.sprite import Group
from raindrop import Raindrop


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Rain")

    raindrop_image = pygame.image.load("raindrop.png")
    raindrops = Group()

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Watch for keyboard and mouse events.
        screen.fill((0, 0, 0))

        # Render all stars
        for raindrop in raindrops:
            raindrop.update()
            raindrop.blitme()
            if raindrop.rect.y > 768:
                raindrops.remove(raindrop)

        # Repopulate raindrops
        if len(raindrops) < 25:
            for x in range(random.randint(0, 10)):
                raindrop = Raindrop(screen, raindrop_image, random.randint(0, 1024), random.randint(0, 768))
                raindrops.add(raindrop)

        # Redraw the screen during each pass through the loop
        pygame.display.flip()


run_game()
