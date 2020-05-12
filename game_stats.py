class GameStats:
    """Track statistics for Alien Invasion game."""

    def __init__(self, ai_game):
        """Init statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Game over flag
        self.game_over = False

        # Read high score from file.
        self.file_name = 'high_score.dat'
        try:
            with open(self.file_name, 'r') as f:
                self.high_score = f.read()

            try:
                self.high_score = int(self.high_score)
            except ValueError:
                self.high_score = 0

        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Reset statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save high score to file."""
        try:
            with open(self.file_name, 'w') as f:
                f.write(str(self.high_score))
        except:
            print(f"ERROR: Cannot open file {self.file_name} for writing.")