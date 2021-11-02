import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class to manage the bullets fired by ship
    """

    def __init__(self, ai_game, *groups):

        """Creating bullet object at ships's current position"""

        super().__init__(*groups)  # *groups is arbitarry num. Can be zero or more that zero

        self.screen = ai_game.screen
        # here we dont need to get rect of screen, as we
        # are going to directly draw the rect on bullet on

        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # rect for bullet
        # In ship module we created a rect using the loaded image
        # but here, we create a empty rect from scrach. Later we can fill it with desired color
        # 0,0 is the initial position. we will reset it in next line
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        # resetting starting position of bullet
        self.rect.midbottom  = ai_game.ship.rect.midbottom

        # Position after bullets leaves starting position
        # and travels in y-axis acccording to the speed value
        # storing that value in decimal form
        self.y = self.rect.y
        # taking the y-axis attribute of bullet's rect, and assigning it to a new attribute
        # so we can do calculations in float form

    def update(self):

        # value for bullet moving up (in y-axis) at given speed
        # while doing this calculation, if we use float the later truncated value will be more accurate
        # for eg. float(1.6) + float(1.6) ~ int(3) this is better if we do calc in float
        # rather that, 1.6 + 1.6 = 2 + 2 = int(4) if we dont do calc in float
        self.y -= float(self.settings.bullet_speed)

        # updating bullet's rect with above value
        # self.rect.y is the position of self.rect on y axis. it also has self.rect.x but we dont need to chage it.
        self.rect.y = self.y

    def draw_bullet(self):

        # draw bullet on screen
        # pygame.draw retuns/draws a rect,
        # in this case will return a colored rect
        pygame.draw.rect(self.screen, self.color, self.rect)
        # this will return the a rect copy of self.rect at its specific position
        # and blit it to on self.screen with self.color filled
        # check docs => http://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        # screen.blit vs pygame.draw.rect => https://stackoverflow.com/questions/17454257/a-bit-confused-with-blitting-pygame
