import json
import pygame.font


class Scoreboard:

    def __init__(self, wa_game):
        self.wa_game = wa_game
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.score = 0
        self.hight_score = 0
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 52)
        self.meat = pygame.image.load('images/meat.png')
        self.meat_rect = self.meat.get_rect()
        self.meat_rect.right = self.screen_rect.right - 90
        self.meat_rect.top = 140
        self.second_meat_rect = self.meat.get_rect()
        self.second_meat_rect.right = self.screen_rect.right - 90
        self.second_meat_rect.top = 80
        self.path = 'record.json'
        self.record = 0
        self.load_record()

    def create_score(self):
        score_str = format(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 140
        self.score_rect.top = 140
        hight_score_str = format('hight score: ' + str(self.hight_score))
        self.hight_score_image = self.font.render(hight_score_str, True,
                                                  self.text_color)
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.right = self.screen_rect.right - 140
        self.hight_score_rect.top = 80

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.meat, self.meat_rect)
        self.screen.blit(self.meat, self.second_meat_rect)

    def load_record(self):
        with open(self.path) as f:
            self.record = int(json.load(f))
            self.hight_score = self.record

    def save_record(self):
        if self.record < self.hight_score:
            with open(self.path, 'w') as f:
                json.dump(self.hight_score, f)
