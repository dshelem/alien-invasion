class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Init the game's static settings."""
        # Window settings.
        self.caption = "Alien Invasion"

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 191, 255)
        # Full screen?
        self.full_screen = False

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        self.bullet_color = (254, 27, 7)
        # self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        # Fleet seetings.
        self.fleet_drop_speed = 10

        # Game settings
        # Seconds to pause after the ship was hit
        self.pause = 1.0

        # How quickly the game speeds up.
        self.speedup_scale = 1.3

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        # Sound settings
        self.music_volume = 0.4
        self.sound_on = True

        # Setting/resetting dynamic values
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game."""
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 1.5
        # Fleet direction: 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_game_speed(self):
        """Increase game speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
