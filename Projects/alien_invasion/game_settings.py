import pygame

class Settings:
    """
    Class to store all the settings for the game in only module
    """

    def __init__(self) -> None:
        """
        initialize all game settings
        """

        # game window settings
        self.screen_width = 1000  
        self.screen_height = 1000
        self.bg_color = (0, 0, 0) 

        # window caption and icon
        self.caption = "Alien Invasion"
        self.icon = pygame.image.load('images/ufo2.png') 

        # ship speed
        self.ship_speed = 0.8

        # bullet settings
        self.bullet_height = 12
        self.bullet_width = 5
        self.bullet_speed = 1.2
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        