import pygame as py

import ship_module

class ScoreCard:
    """Class to report scoring information"""

    def __init__(self, ai_game):
        """initialize score keeping attributes"""

        # for ship group
        self.ai_game = ai_game

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

        # ALL the default values are prepped wen game starts and calls scorecard class

        # prepare initial score image
        self.prep_score()

        # prepare image of high scoreset previously
        self.prep_high_score()

        # prepare level image
        self.prep_level()

        # self.prep_ship()
        self.prep_ship()


    def prep_score(self):
        """prep image of the score"""

        rounded_score = round(self.stats.score, -1)

        # store the score from stats module in a string
        score_str = f'{rounded_score:,}'

        # create an image of the score string
        self.score_image = self.font1.render(
            score_str, True,self.text_color, self.settings.bg_color)

        # Display the score on top right of the screen

        # create/get rect of the image
        self.score_rect = self.score_image.get_rect()

        # setting position
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """prep image of high score at top center of the screen"""

        rounded_high_score = round(int(self.stats.high_score), -1)

        # store the rounded high score string in a variable and format it with commas as required
        high_score_str = f'High Score - {rounded_high_score:,}'

        # create image of high score string
        self.high_score_image = self.font1.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        # get rect of this image
        self.high_score_image_rect = self.high_score_image.get_rect()

        # set position
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_rect.top


    def prep_level(self):
        """prepare image of level to later draw on screen"""

        # get level in string format
        level_str = str(self.stats.level)
        level_str = f'Level - {level_str}'

        # create image of level
        self.level_image = self.font1.render(
            level_str, True, self.text_color, self.settings.bg_color)

        # get the level_image's rect and set its position
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.bottom = self.score_rect.bottom + 25

    def prep_ship(self):
        """prep image of available ships"""

        # prepare group to store ship sprites
        self.ship_group = py.sprite.Group()

        # prepping ship's positions and adding them to the above ship's sprite group
        for ship_number in range(self.stats.ship_left):

            # create a ship sprite. i.e. creating ship using ship class using game instance(ai_game)
            # as ship class's init takes 2 args (self, ai_game)
            # so we set self.ai_game = ai_game in init of scorecard to we can use it here
            ship = ship_module.Ship(self.ai_game)

            # settings x axis value. eg. ship 1st will take position => 10 + (1*ship.rect.width)
            # then 2nd ship will take position => 10 + (2*ship.rect.width)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10

            # add the ship sprite with x,y axis modified into the group
            self.ship_group.add(ship)


    def check_high_score(self):
        """check if new high score created. prep that and update the file"""

        if self.stats.score > int(self.stats.high_score):

            # set the new score as high score
            self.stats.high_score = self.stats.score

            # prepare new value of the high score. show_score() will blit this new value
            self.prep_high_score()

            # write this new high score in the file which will new loaded new time u run the game
            with open("high_score.txt", 'w') as f:
                f.write(str(self.stats.high_score))


    def show_score(self):
        """drawing score image, high score image, level image, ships sprites on screen"""

        # draw current and high scores on screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ship_group.draw(self.screen)
