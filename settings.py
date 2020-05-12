import json

class Settings:
    """A class to store all settings for the game."""

    SHIP_SPEED = 5
    BULLET_SPEED = 5
    ALIEN_SPEED = 1.5
    ALIEN_POINTS = 50

    def __init__(self):
        """Init the game's static settings."""
        # Window settings.
        self.caption = "Alien Invasion"

        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 191, 255)
        # Full screen?
        self.full_screen = False

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullets_allowed = 7

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

        # Try to load sound_on setting from file
        self.file_name = 'settings.json'
        try:
            with open(self.file_name, 'r') as f:
                self.sound_on = json.load(f)
        except FileNotFoundError:
            self.sound_on = True

        # Show FPS during the game
        self.show_fps = False

        # Setting/resetting dynamic values
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game."""
        self.ship_speed = self.SHIP_SPEED
        self.bullet_speed = self.BULLET_SPEED
        self.alien_speed = self.ALIEN_SPEED
        # Fleet direction: 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = self.ALIEN_POINTS

    def increase_game_speed(self):
        """Increase game speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def save_settings(self):
        """Save storable settings to file."""
        try:
            with open(self.file_name, 'w') as f:
                json.dump(self.sound_on, f)
        except:
            print(f"ERROR: Cannot open file {self.file_name} for writing.")