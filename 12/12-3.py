import sys
import pygame


def check_keydown_events(event, rocket):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True


def check_keyup_events(event, rocket):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


class Rocket:
    def __init__(self, screen):
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('rocket.jpg')
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 2
        if self.moving_left and self.rect.left > 0:
            self.centerx -= 2
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 2

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def blitme(self, screen):
        screen.blit(self.image, self.rect)


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 786))

    rocket = Rocket(screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        check_events(rocket)

        # Up date ship
        rocket.update()

        # Redraw the screen during each pass through the loop
        screen.fill((255, 255, 255))
        rocket.blitme(screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
