from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, screen, star_image):
        super(Star, self).__init__()
        self.screen = screen
        self.star_image = star_image
        self.rect = star_image.get_rect()

    def blitme(self):
        self.screen.blit(self.star_image, self.rect)
