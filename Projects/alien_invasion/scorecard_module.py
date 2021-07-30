import pygame.font

import game_settings

import stats_module

class ScoreCard:
    """Class to report scoring information"""

    def __init__(self, ai_game) -> None:
        """initialize score keeping attributes"""

        # get the main screen
        self.screen = ai_game.screen

        # get the settings 
        self.settings = game_settings.Settings()

        # stats module to get the score stat
        self.stats =  stats_module.Stats()

        # score text color and font
        self.color_score_text = (255,255,255)
        self.score_font = pygame.font.SysFont(None, 30)

        # prepare initial score image
        self.score_image()

    
    def score_image(self):
        """create image of the score"""

        # store the score from stats module in a string
        self.score_str = str(self.stats.score)

        # create an image of the score string
        self.score_image = self.score_font.render(
            self.score_str, True,self.color_score_text, self.settings.bg_color)

        # Display the score on top right of the screen

        # create/get rect of the image
        self.score_rect = self.score_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # setting position
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """blit/draw the score image from above on screen"""
        self.screen.blit(self.score_image, self.score_rect)












    
