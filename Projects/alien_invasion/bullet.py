import game_settings
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Class to manage the bullets fired by ship
    """        
    
    def __init__(self, ai_game, *groups):
        super().__init__(*groups)

        # Creating bullet object at ships's current position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # rect for bullet
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)

        # resetting starting position of bullet
        self.rect.midbottom = ai_game.ship.rect.midbottom

        # Position for bullet stored as decimal
        self.y = float(self.rect.y)


    def update(self):

        # value for bullet moving up (in y-axis) at given speed
        self.y -= self.settings.bullet_speed

        # updating bullet's rect with above value
        self.rect.y = self.y

    def draw_bullet(self):

        # draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)

