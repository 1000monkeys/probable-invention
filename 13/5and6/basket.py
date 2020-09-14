import pygame
from pygame.rect import Rect


class Basket():
    def __init__(self, screen):
        self.screen = screen
        self.rect = Rect(512, 740, 250, 25)

    def draw(self):
        pygame.draw.rect(self.screen, (220, 220, 220), self.rect)

    def update(self, left_pressed, right_pressed):
        if left_pressed and self.rect.left > 0:
            self.rect.x -= 1
        if right_pressed and self.rect.right < 1024:
            self.rect.x += 1
