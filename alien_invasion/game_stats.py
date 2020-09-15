import json


class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        hs = 0
        try:
            with open('score.txt') as json_file:
                data = json.load(json_file)
                hs = data
        except FileNotFoundError:
            hs = 0

        self.high_score = hs

        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
