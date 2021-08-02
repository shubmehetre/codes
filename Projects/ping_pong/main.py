from _typeshed import Self
import pygame

import settings

class Main:
    """main ping pong class"""

    def __init__(self) -> None:
        """initialize main components of ping pong"""

        # init pygame
        pygame.init()

        # get all settings
        self.settings = settings.Settings()

        # Create main screen for gamea
        self.screen = pygame.display.set_mode(
            self.settings.screen_width, self.settings.screen_height)

        self

        