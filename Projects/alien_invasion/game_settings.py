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
        self.screen_width = 700  
        self.screen_height = 800
        self.bg_color = (0, 0, 0) 

        # window caption and icon
        self.caption = "Alien Invasion"
        self.icon = pygame.image.load('images/ufo2.png') 

        # ship speed
        self.speed = 0.35

        # bullet settings
        self.bullet_height = 10
        self.bullet_width = 3
        self.bullet_speed = 1.0
        self.bullet_color = (60,60,60)

        