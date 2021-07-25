import game_settings

class Stats:
    """track stats of Alien Invasion"""

    def __init__(self) -> None:
        """initialize stats"""
        self.settings = game_settings.Settings()

        # auto method called to reset stats
        self.reset_stats()


    def reset_stats(self):
        """initialize stats that change during game"""

        self.ship_left = game_settings.Settings.ship_limit

