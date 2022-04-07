import pygame

from pygame.sprite import Sprite


class Boar(Sprite):

    def __init__(self, wa_game):
        super().__init__()
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.wolf = wa_game.wolf
        self.boar = [
            pygame.image.load('images/boar_1.png'),
            pygame.image.load('images/boar_2.png'),
            pygame.image.load('images/boar_3.png'),
            pygame.image.load('images/boar_4.png'),
            pygame.image.load('images/boar_5.png'),
            pygame.image.load('images/boar_6.png')
        ]
        self.rect = self.boar[0].get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.bottomleft = (self.screen_rect.width * 1.1,
                                self.screen_rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.boar_speed = 0.8
        self.animation_count = 0

    # Boar movement
    def update(self):
        if self.wolf.moving_right:
            self.boar_speed = 1.2
            self.x -= self.boar_speed
        if self.wolf.moving_left:
            self.boar_speed = 0.4
            self.x -= self.boar_speed
        else:
            self.boar_speed = 0.8
            self.x -= self.boar_speed
        self.rect.x = self.x

    # Drawing boar
    def blitme(self):
        if self.animation_count + 1 >= 120:
            self.animation_count = 0
        self.screen.blit(self.boar[self.animation_count // 30], self.rect)
        self.animation_count += 1
