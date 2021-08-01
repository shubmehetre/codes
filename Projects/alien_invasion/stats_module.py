import game_settings

class Stats:
    """track stats of Alien Invasion"""

    def __init__(self, ai_game) -> None:
        """initialize stats"""
        self.settings = ai_game.settings

        # auto method called to reset stats
        self.reset_stats()

        # flag to keep game running
        self.game_running = False


        # high score (only resets if broken)
        high_score_file = "high_score.txt"
        
        with open(high_score_file) as f:
            self.high_score = f.read()

        
    def reset_stats(self):
        """initialize stats that change during game"""

        # replenishing ship's left stat when this method is called
        self.ship_left = self.settings.ship_limit
        
        # reset score
        self.score = 0

        # Level 
        self.level = 1


