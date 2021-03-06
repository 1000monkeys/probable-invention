from pygame.sprite import Sprite
import random

class Raindrop(Sprite):
    def __init__(self, screen, raindrop_image, start_x, offset_y):
        super(Raindrop, self).__init__()
        self.screen = screen
        self.raindrop_image = raindrop_image
        self.rect = raindrop_image.get_rect()
        self.rect.x = start_x
        self.rect.y -= offset_y
        self.y = float(self.rect.y)
        self.speed = random.randint(0, 10) / 10

    def update(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def blitme(self):
        self.screen.blit(self.raindrop_image, self.rect)
