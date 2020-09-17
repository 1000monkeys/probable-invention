import pygame
import random

from pygame.rect import Rect


class Ball():
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(10, 1014)
        self.y = 0
        self.rect = Rect(self.x, self.y, 5, 5)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 5)

    def update(self):
        self.y += 1
        self.rect.y = self.y
