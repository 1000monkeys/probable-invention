import sys
import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 786))

    # Start the main loop for the game.
    while True:
        # Respond to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill screen with blue color
        screen.fill((0, 0, 255))

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
