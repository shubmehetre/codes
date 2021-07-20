import sys

import pygame

import game_settings

import ship_module

class AlienInvasion:
    """
    Class to manage game assets and behavior 
    """

    def __init__(self) -> None:
        
        # initializes all pygame modules
        pygame.init()

        # create instance for settings module
        self.settings = game_settings.Settings()

     
        # Surface - part of screen where game elements are displayed
        # Here display.set_mode is surface for entire game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # for full sceen use this:
#       self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#       self.settings.screen_width = self.screen.get_rect().width
#       self.settings.screen_height = self.screen.get_rect().height

        # set caption and icon for window
        pygame.display.set_caption(self.settings.caption) 
        pygame.display.set_icon(self.settings.icon)

        # ship module initialization
        self.ship = ship_module.Ship(self)

    def run_game(self):
        """
        start main loop for game
        """
        running = True

        # running game window infinitely until QUIT event is triggered
        while running:
            
            # helper method to check for events
            self._check_events()

            # update ships position according to keypresses
            self.ship.update()

            # helper method to update screen
            self._update_screen()


    def _check_events(self)    :
            # watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)

            elif event.type == pygame.KEYUP:
                self._key_up_events(event)
    
    def _key_down_events(self, event):
        # 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):

            # window's background color
            self.screen.fill(self.settings.bg_color)

            # blit(draw on screen) the ship on screen
            self.ship.blitme()

            # make most recently drawn screen visible
            # continually updates display to show new positions of objects
            pygame.display.flip()


if __name__ == "__main__":

    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()



    