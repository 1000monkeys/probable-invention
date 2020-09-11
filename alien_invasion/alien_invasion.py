import pygame
from ai_settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship, ai_settings, screen, bullets)

        # Up date ship
        ship.update()

        gf.update_bullets(bullets)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()