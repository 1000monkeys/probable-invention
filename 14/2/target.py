import pygame
from pygame.rect import Rect


class Target:
    def __init__(self, screen, ship):
        self.screen = screen
        self.ship = ship
        self.screen_rect = screen.get_rect()
        self.rect = Rect(self.ship.rect.left, self.ship.rect.top, 10, 10)
        self.x = self.screen_rect.right - 50
        self.rect.x = self.x
        self.y = self.screen_rect.centery
        self.direction = 1

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 50)

    def update(self):
        if self.y > self.screen_rect.bottom or self.y < self.screen_rect.top:
            self.direction *= -1

        self.y += self.direction
        self.rect.y = self.y
