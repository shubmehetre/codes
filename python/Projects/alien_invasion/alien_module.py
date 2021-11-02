import pygame

from pygame.sprite import Sprite
# from alien_invasion import AlienInvasion


class Alien(Sprite):
    def __init__(self, ai_game) -> None:
        """class to manage the aliens in game"""

        # initializing Sprite
        super().__init__()

        # getting the main screen
        self.screen = ai_game.screen

        # we get the main screen rect here to set position of ship 
        # and also to tell ship not to go beyond the main screen
        self.screen_rect = ai_game.screen.get_rect()

        # getting settings
        self.settings = ai_game.settings

        # loading the alien image in a variable
        # and creating a rect of size of the image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # setting initial position of one alien
        self.rect.x = self.rect.width  
        self.rect.y = self.rect.height 

        # storing exact horizonal position of alien we take 
        # the main x attribute in another varible to do calculation
        self.x = float(self.rect.x)

    
    def update(self):
        """moving the aliens"""

        self.x += (self.settings.alien_speed
                    * self.settings.fleet_direction)

        self.rect.x = self.x


    def check_edges(self):
        """check if the aliens hits edge of screen"""

        # screen_rect = self.screen.get_rect()

        if self.rect.right >= self.screen_rect.right or self.rect.left == 0:
            return True






















