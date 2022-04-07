import pygame

from pygame.sprite import Sprite


class Meat(Sprite):

    def __init__(self, wa_game):
        super().__init__()
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.wolf = wa_game.wolf
        self.meat = pygame.image.load('images/meat.png')
        self.rect = self.meat.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.bottomleft = (self.screen_rect.width / 1.5,
                                self.screen_rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # Meat movement
    def update(self):
        if self.wolf.moving_right:
            self.x -= self.wolf.speed_bg_scrolling
        if self.wolf.moving_left:
            self.x += self.wolf.speed_bg_scrolling
        self.rect.x = self.x

    # Drawing meat
    def blitme(self):
        self.screen.blit(self.meat, self.rect)
