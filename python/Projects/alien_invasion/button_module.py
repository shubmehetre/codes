import game_settings

import pygame

class Button:
    """start game button rect"""

    def __init__(self, ai_game,msg) -> None:
        """initialize the button"""

        # getting the main screen to draw the button rect on
        self.screen = ai_game.screen

        # init the settings module
        self.settings = game_settings.Settings()

        # setting color of button
        self.button_color = ai_game.settings.button_color
        self.text_color = ai_game.settings.text_color
        self.text_font = pygame.font.SysFont(None, 48)

        # Creating a rect and setting position of the button
        self.rect = pygame.Rect(0,0, self.settings.button_width, self.settings.button_height)
        self.rect.center = self.screen.get_rect().center

        # button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn the msg provided to an image to draw in screen"""

        # converting the text into a image of that text
        self.msg_image = self.text_font.render(msg, True, self.text_color, self.button_color)

        # create a rect of the above image size 
        self.msg_image_rect = self.msg_image.get_rect()

        # place the image of the text in the centre of the button
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):

        # fill the button's rect with button color
        self.screen.fill(self.button_color, self.rect)

        # draw the msg on screen
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
