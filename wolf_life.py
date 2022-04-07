import pygame

from pygame.sprite import Sprite


class WolfLife(Sprite):

    def __init__(self, wa_game):
        super().__init__()
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.wolf_life = pygame.image.load('images/wolf_life.png')
        self.rect = self.wolf_life.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Drawing wolf life
    def blitme(self):
        self.screen.blit(self.wolf_life, self.rect)
