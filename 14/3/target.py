import pygame
from pygame.rect import Rect


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.x = self.screen_rect.right - 50
        self.y = self.screen_rect.centery
        self.direction = 1
        self.rect = Rect(self.x - 50, self.y, 100, 100)
        self.rect.x = self.x

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), 50)

    def update(self):
        if self.y > self.screen_rect.bottom or self.y < self.screen_rect.top:
            self.direction *= -1

        self.y += self.direction * self.speed
        self.rect.y = self.y - 50

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed
