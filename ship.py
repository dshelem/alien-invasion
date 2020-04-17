import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game, extra_small=False):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Reference to settings instance.
        self.settings = ai_game.settings

        # Extra small image of ship is used for scoreboard
        if extra_small:
            self.file_name = 'img/ship_xxs.png'
        else:
            self.file_name = 'img/ship_small.png'

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.file_name)
        self.rect = self.image.get_rect()

        self._moving_left = False
        self._moving_right = False

        self.x = float(self.rect.x)

        self.center_ship()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def _delta_position(self):
        """Returns ship speed."""
        # self._seconds_moving = time.perf_counter() - self._start_time
        # if self._seconds_moving <= 0.5:
        #     return 2.0
        # elif self._seconds_moving <= 1.5:
        #     return 3.0
        # elif self._seconds_moving <= 2.5:
        #     return 5.0
        # else:
        #     return 6.0
        return self.settings.ship_speed

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self._moving_right and self.rect.right < self.screen_rect.right:
            self.x += self._delta_position()
        if self._moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self._delta_position()

        self.rect.x = self.x

    def move_right(self):
        """Sets moving right flag to true and starts timer."""
        self._moving_right = True

    def move_left(self):
        """Sets moving right flag to true and starts timer."""
        self._moving_left = True

    def stop_moving(self):
        """Sets moving right & left flags to false."""
        self._moving_left = False
        self._moving_right = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.stop_moving()