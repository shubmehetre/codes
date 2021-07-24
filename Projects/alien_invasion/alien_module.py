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

        # loading the alien image in a variable
        # and creating a rect of size of the image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # setting initial position of the alien
        # self.rect.topleft = self.screen_rect.topleft
        self.rect.x = self.rect.width / 2 
        self.rect.y = self.rect.height / 2

        # storing exact horizonal position of alien
        self.x = float(self.rect.x)


    # def blitme(self):
    #     """blits the image with the rect on the main screen"""

    #     self.screen.blit(self.image, self.rect)
