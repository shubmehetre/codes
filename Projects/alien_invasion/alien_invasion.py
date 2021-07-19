import sys
import pygame
import game_settings

class AlienInvasion:
    """
    Class to manage game assets and behavior 
    """

    def __init__(self) -> None:
        
        # initializes all pygame modules
        pygame.init()
        
        # called the Surface - part of screen where game element is displayed
        # here display.set_mode is surface for entire game window
        self.screen = pygame.display.set_mode((800, 600))  # screen for game
        pygame.display.set_caption("Alien Invasion")  # caption of game window

        icon = pygame.image.load('ufo.png')  # load a image in a variable 
        pygame.display.set_icon(icon)  # set the loaded image as icon for the game

        self.settings = game_settings.Settings()

    def run_game(self):
        """
        start main loop for game
        """

        running = True
        while running:
            # watch keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()              # use sys for system functions

            # make most recently drawn screen visible
            # continually updates display to show new positions of objects
            pygame.display.flip()
            
            self.screen.fill(game_settings.Settings.)

if __name__ == "__main__":

    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()



    