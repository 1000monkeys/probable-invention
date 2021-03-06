import pygame
from ai_settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(screen, "Play")

    # Make a group to store bullets in.
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # Update ship
            ship.update()
            # Update bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Update aliens
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
