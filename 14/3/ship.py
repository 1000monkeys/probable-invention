import pygame


class Ship:
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centery)

        # Movement flag
        self.up_pressed = False
        self.down_pressed = False

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.up_pressed and self.rect.top > 0:
            self.center -= 1

        if self.down_pressed and self.rect.bottom < self.screen_rect.bottom:
            self.center += 1

        self.rect.centery = self.center

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centery
