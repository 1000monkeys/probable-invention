import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.centery = ship.rect.centery
        self.rect.centerx = ship.rect.centerx

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

        self.color = (0, 0, 0)
        self.speed_factor = 1

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
