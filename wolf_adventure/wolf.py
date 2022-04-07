import pygame


class Wolf:

    def __init__(self, wa_game):
        self.screen = wa_game.screen
        self.screen_rect = wa_game.screen.get_rect()
        self.wolf_stand = pygame.image.load('images/wolf_stand.png')
        self.wolf_stand_left = pygame.image.load('images/wolf_stand_left.png')
        self.walk_right = [
            pygame.image.load('images/right_1.png'),
            pygame.image.load('images/right_2.png'),
            pygame.image.load('images/right_3.png'),
            pygame.image.load('images/right_4.png'),
            pygame.image.load('images/right_5.png'),
            pygame.image.load('images/right_6.png'),
            pygame.image.load('images/right_7.png')
        ]
        self.walk_left = [
            pygame.image.load('images/left_1.png'),
            pygame.image.load('images/left_2.png'),
            pygame.image.load('images/left_3.png'),
            pygame.image.load('images/left_4.png'),
            pygame.image.load('images/left_5.png'),
            pygame.image.load('images/left_6.png'),
            pygame.image.load('images/left_7.png')
        ]
        self.jump_right = [
            pygame.image.load('images/jump_right_1.png'),
            pygame.image.load('images/jump_right_2.png'),
            pygame.image.load('images/jump_right_3.png'),
            pygame.image.load('images/jump_right_4.png')
        ]
        self.jump_left = [
            pygame.image.load('images/jump_left_1.png'),
            pygame.image.load('images/jump_left_2.png'),
            pygame.image.load('images/jump_left_3.png'),
            pygame.image.load('images/jump_left_4.png')
        ]
        self.rect = self.wolf_stand.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.midbottom = (self.screen_rect.width / 4,
                               self.screen_rect.height)
        self.wolf_bottom = self.rect.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.wolf_look_left = False
        self.bg_scrolling_left = False
        self.bg_scrolling_right = False
        self.jump = False
        self.after_jump = False
        self.jump_top = self.screen_rect.height - self.screen_rect.height / 4.2
        self.pos_x = 0
        self.speed_bg_scrolling = 1.6
        self.wolf_speed = 1.2
        self.wolf_speed_jump = 2.2
        self.animation_count = 0

    # Wolf movement
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.width / 2:
            self.x += self.wolf_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.wolf_speed
        if self.jump and self.y > self.jump_top:
            self.y -= self.wolf_speed_jump
            self.after_jump = True
        else:
            self.jump = False
            if self.after_jump and self.y < self.wolf_bottom:
                self.y += self.wolf_speed_jump
            else:
                self.after_jump = False
        self.rect.x = self.x
        self.rect.y = self.y

    # Drawing wolf
    def blitme(self):
        if self.animation_count + 1 >= 140:
            self.animation_count = 0
        elif self.moving_right:
            if self.jump:
                self.screen.blit(
                    self.jump_right[self.animation_count // 35], self.rect
                )
                self.animation_count += 1
            else:
                self.screen.blit(
                    self.walk_right[self.animation_count // 20], self.rect
                )
                self.animation_count += 1
        elif self.moving_left:
            if self.jump:
                self.screen.blit(
                    self.jump_left[self.animation_count // 35], self.rect
                )
                self.animation_count += 1
            else:
                self.screen.blit(
                    self.walk_left[self.animation_count // 20], self.rect
                )
                self.animation_count += 1
        elif self.wolf_look_left:
            if self.jump:
                self.screen.blit(
                    self.jump_left[self.animation_count // 35], self.rect
                )
                self.animation_count += 1
            else:
                self.screen.blit(self.wolf_stand_left, self.rect)
        elif self.jump:
            self.screen.blit(
                self.jump_right[self.animation_count // 35], self.rect
            )
            self.animation_count += 1
        else:
            self.screen.blit(self.wolf_stand, self.rect)

    def scrolling_bg(self):
        if self.bg_scrolling_left:
            self.pos_x -= self.speed_bg_scrolling
        if self.bg_scrolling_right and self.rect.left > 0:
            self.pos_x += self.speed_bg_scrolling
