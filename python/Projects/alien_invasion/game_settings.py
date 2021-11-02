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

        # ship settings
        self.ship_limit = 2

        # bullet settings
        self.bullet_height = 12
        self.bullet_width = 5
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_drop_speed = 30
        # self.alien_direction = 1

        # button settings
        self.button_color = (50, 40, 100)
        self.button_width = 100
        self.button_height = 60
        self.text_color = (255,255,255)

        # Level ups
        self.speedup_scale = 1.2

        # alien points increase scale
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """new settings for new level"""

        # initial game element's speed settings
        self.ship_speed = 1.2
        self.bullet_speed = 1.6
        self.alien_speed = 0.4

        # points
        self.alien_points = 12
        
        # 1 is to right and -1 is to left
        self.fleet_direction = 1


    def game_speed_increase(self):
        """asd"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # print(self.alien_points) this looks ok
        
        self.alien_points  = int(self.alien_points * self.score_scale)
