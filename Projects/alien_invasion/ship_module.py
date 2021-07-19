import pygame as py
import game_settings as gs

class Ship:
    """
    class to manage the ship in game
    """

    # we pass instance of AlienInvasion class in Ship's init
    # so that we can access all stuff from main code
    def __init__(self, ai_game) -> None:
        """
        initialize the ship and set starting position
        """
        
        # returns screen surface
        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        # load ship's image and get its rect

        # returns surface representing the ship
        self.image = py.image.load('images/ship.bmp')
        # access the returned surface's rect value using get_rect
        self.rect = self.image.get_rect()
        
        # Ship's starting position
        self.rect.midbottom = self.screen_rect.midbottom

        # moving of ship
        self.moving_right = False
        self.moving_left = False

        # creating settings module object
        self.settings = gs.Settings()

        # converting ships horizontal position value into decimal
        self.x = float(self.rect.x)

    def update(self):
        """
        update ships position based on moving_left/right flags
        This method will be called infinitely in run_game()
        """

        # 'if True' runs only once
        # 'while True' runs infinitely
        if self.moving_right:
            # self.rect.x += 1
            self.x += self.settings.speed

        if self.moving_left:
            self.x -= self.settings.speed

        # this will still assign integer part of number
        # but 1.6 + 1.6 ~ 3 is better than 2 + 2 = 4
        self.rect.x = self.x

    def blitme(self):
        """
        Draws ship at its current location
        """

        self.screen.blit(self.image, self.rect)

