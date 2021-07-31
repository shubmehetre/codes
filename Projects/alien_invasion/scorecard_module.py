import pygame as py

class ScoreCard:
    """Class to report scoring information"""

    def __init__(self, ai_game):
        """initialize score keeping attributes"""

        # get the main screen
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # WRONG WAY
        # self.settings = game_settings.Settings()
        
        # RIGHT WAY to get the settings 
        self.settings = ai_game.settings

        # stats module to get the score stat
        self.stats =  ai_game.stats

        # score text color and font
        self.text_color = (255,255,255)
        self.font1 = py.font.SysFont(None, 30)

        # prepare initial score image
        self.prep_score()

        # self.prep_ship()

    
    def prep_score(self):
        """prep image of the score"""

        # store the score from stats module in a string
        score_str = str(self.stats.score)

        # create an image of the score string
        self.score_image = self.font1.render(
            score_str, True,self.text_color, self.settings.bg_color)

        # Display the score on top right of the screen

        # create/get rect of the image
        self.score_rect = self.score_image.get_rect()
        
        # setting position
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        """draw the score image from above on screen"""
        self.screen.blit(self.score_image, self.score_rect)

        # self.screen.blit(self.ship_image, self.ship_image_rect)
        # print(self.stats.score)


    # def prep_ship(self):
    #     """prep image of available ships"""

    #     # load the ship image and get its rect
    #     self.ship_image = py.image.load('images/ship.bmp')
    #     self.ship_image_rect = self.ship_image.get_rect()

    #     self.ship_image_rect.left = self.screen_rect.left + 20
    #     self.ship_image_rect.top = 20













    
