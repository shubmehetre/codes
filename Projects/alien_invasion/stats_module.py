import game_settings

class Stats:
    """track stats of Alien Invasion"""

    def __init__(self) -> None:
        """initialize stats"""
        self.settings = game_settings.Settings()

        # auto method called to reset stats
        self.reset_stats()

        # flag to keep game running
        self.game_running = False

        
    def reset_stats(self):
        """initialize stats that change during game"""

        # replenishing ship's left stat when this method is called
        self.ship_left = self.settings.ship_limit

