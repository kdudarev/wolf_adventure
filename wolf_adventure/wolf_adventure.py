import pygame
import random
import sys

from boar import Boar
from buttons import Buttons
from meat import Meat
from scoreboard import Scoreboard
from time import sleep
from wolf import Wolf
from wolf_life import WolfLife


class WolfAdventure:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg = pygame.transform.smoothscale(
            pygame.image.load('images/bg.png'),
            (self.screen_width, self.screen_height)
        )
        self.first_bg = 0
        self.second_bg = 0
        self.game_active = False
        self.buttons = Buttons(self)
        self.sb = Scoreboard(self)
        self.wolf = Wolf(self)
        self.wolf_limit = 3
        self.wolf_lifes = pygame.sprite.Group()
        self.boars = pygame.sprite.Group()
        self.meat_sprites = pygame.sprite.Group()
        self.new_meat_list = False
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.wolf.update()
                self.wolf.scrolling_bg()
                self._boars_run()
                self._check_wolf_boar_collisions()
                self._check_wolf_meat_collisions()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_push_button(mouse_pos)
        self.first_bg = self.wolf.pos_x % self.screen_width
        if self.first_bg > 0:
            self.second_bg = self.first_bg - self.screen_width
        else:
            self.second_bg = self.first_bg + self.screen_width

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.wolf.moving_right = True
            self.wolf.bg_scrolling_left = True
            self.wolf.wolf_look_left = False
        elif event.key == pygame.K_LEFT:
            self.wolf.moving_left = True
            self.wolf.bg_scrolling_right = True
        elif event.key == pygame.K_SPACE:
            self.wolf.jump = True
        elif event.key == pygame.K_ESCAPE:
            self.sb.save_record()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.wolf.moving_right = False
            self.wolf.bg_scrolling_left = False
        elif event.key == pygame.K_LEFT:
            self.wolf.moving_left = False
            self.wolf.bg_scrolling_right = False
            self.wolf.wolf_look_left = True

    def _check_push_button(self, mouse_pos):
        play_button_clicked = self.buttons.p_rect.collidepoint(mouse_pos)
        quit_button_clicked = self.buttons.q_rect.collidepoint(mouse_pos)
        if play_button_clicked and not self.game_active:
            self.start_game()
        if quit_button_clicked and not self.game_active:
            sys.exit()

    def start_game(self):
        self.game_active = True
        self.boars.empty()
        self.meat_sprites.empty()
        self.wolf_limit = 3
        self.sb.create_score()
        self.wolf.x = self.screen_width / 4
        self._create_boars()
        self._create_meat()
        self._create_wolf_lifes()
        pygame.mouse.set_visible(False)

    def _create_wolf_lifes(self):
        position = 80
        for life in range(self.wolf_limit):
            wolf_life = WolfLife(self)
            wolf_life.x = position
            wolf_life.rect.x = wolf_life.x
            position += 90
            self.wolf_lifes.add(wolf_life)

    def _create_meat(self):
        position = self.screen_width / 1.5
        new_position = self.screen_width * 1.1
        for i in range(10):
            meat = Meat(self)
            if self.new_meat_list:
                meat.x = new_position
            else:
                meat.x = position
            meat.rect.x = meat.x
            position += random.randrange(200, 600)
            new_position += random.randrange(200, 600)
            self.meat_sprites.add(meat)

    def _meat_moving(self):
        for meat in self.meat_sprites.sprites():
            meat.update()
            self._check_border_for_meat(meat)

    def _check_border_for_meat(self, meat):
        if meat.rect.x < -100:
            meat.kill()
        if len(self.meat_sprites.sprites()) == 5:
            self.new_meat_list = True
            self._create_meat()

    def _check_wolf_meat_collisions(self):
        collected = pygame.sprite.spritecollide(self.wolf, self.meat_sprites, True)
        for meat in collected:
            self.sb.score += 1
            if self.sb.hight_score < self.sb.score:
                self.sb.hight_score = self.sb.score
        self.sb.create_score()

    def _create_boars(self):
        position = self.screen_width * 1.1
        for i in range(10):
            boar = Boar(self)
            boar.x = position
            boar.rect.x = boar.x
            position += random.randrange(600, 1100)
            self.boars.add(boar)

    def _check_border_for_boars(self, boar):
        if boar.rect.x < -100:
            boar.kill()
        if len(self.boars.sprites()) == 2:
            self._create_boars()

    def _boars_run(self):
        for boar in self.boars.sprites():
            boar.update()
            self._check_border_for_boars(boar)

    def _check_wolf_boar_collisions(self):
        if pygame.sprite.spritecollideany(self.wolf, self.boars):
            if self.wolf_limit == 1:
                self.game_active = False
                self.boars.empty()
                self.meat_sprites.empty()
                self.wolf_lifes.empty()
                self.sb.score = 0
                pygame.mouse.set_visible(True)
            else:
                self.boars.empty()
                self.meat_sprites.empty()
                self.wolf_lifes.empty()
                self.wolf_limit -= 1
                self._create_wolf_lifes()
                self.wolf.x = self.screen_width / 4
                self._create_boars()
                self._create_meat()
                sleep(0.5)

    def _update_screen(self):
        self.screen.blit(self.bg, (self.first_bg, 0))
        self.screen.blit(self.bg, (self.second_bg, 0))
        if not self.game_active:
            self.buttons.draw_buttons()
        else:
            self.sb.draw_score()
            self.wolf.blitme()
            for life in self.wolf_lifes.sprites():
                life.blitme()
        for boar in self.boars.sprites():
            boar.blitme()
        for meat in self.meat_sprites.sprites():
            meat.blitme()
        self._boars_run()
        self._meat_moving()
        pygame.display.flip()
        self.clock.tick(200)


if __name__ == '__main__':
    wa = WolfAdventure()
    wa.run_game()
