import pygame


class Buttons:

    def __init__(self, wa_game):
        self.screen = wa_game.screen
        self.screen_rect = self.screen.get_rect()
        self.button_play = pygame.image.load('images/play.png')
        self.button_quit = pygame.image.load('images/quit.png')
        self.p_rect = self.button_play.get_rect()
        self.p_rect.x = self.p_rect.width
        self.p_rect.y = self.p_rect.height
        self.p_rect.center = (self.screen_rect.width / 2,
                              self.screen_rect.height / 2.3)
        self.q_rect = self.button_quit.get_rect()
        self.q_rect.x = self.q_rect.width
        self.q_rect.y = self.q_rect.height
        self.q_rect.center = (self.screen_rect.width / 2,
                              self.screen_rect.height / 1.7)

    def draw_buttons(self):
        self.screen.blit(self.button_play, self.p_rect)
        self.screen.blit(self.button_quit, self.q_rect)
