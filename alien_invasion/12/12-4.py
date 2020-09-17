import sys
import pygame


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            print(event)


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 786))

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        check_events()

        # Redraw the screen during each pass through the loop
        screen.fill((255, 255, 255))

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
