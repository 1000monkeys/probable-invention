import sys
import pygame
from pygame.sprite import Sprite, Group


def fire_bullet(screen, bullets, rocket):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < 4:
        new_bullet = Bullet(screen, rocket)
        bullets.add(new_bullet)


def check_events(rocket, screen, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                if event.key == pygame.K_SPACE:
                    fire_bullet(screen, bullets, rocket)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = False


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, 20, 5)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.x = self.rect.x

        self.color = (60, 60, 60)
        self.speed_factor = 3

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = int(self.x)
        self.draw_bullet()

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Rocket:
    def __init__(self, screen):
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.centery = float(self.rect.centery)

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 2

        self.rect.centery = int(self.centery)

    def blitme(self, screen):
        screen.blit(self.image, self.rect)


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    screen = pygame.display.set_mode((1024, 786))
    screen_rect = screen.get_rect()

    bullets = Group()

    rocket = Rocket(screen)

    # Start the main loop for the game.
    while True:
        # Redraw the screen during each pass through the loop
        screen.fill((255, 255, 255))

        # Watch for keyboard and mouse events.
        check_events(rocket, screen, bullets)

        print(len(bullets))

        rocket.update()
        rocket.blitme(screen)

        bullets.update()
        for bullet in bullets.copy():
            if bullet.x > screen_rect.right:
                bullets.remove(bullet)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
