import pygame
import time


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('img/ship_smaller.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self._moving_right = False
        self._moving_left = False
        self._seconds_moving = 0
        self._start_time: float = 0.0

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def _delta_position(self):
        """Returns ship speed on the basis of movement time passed."""
        self._seconds_moving = time.perf_counter() - self._start_time
        if self._seconds_moving <= 0.5:
            return 2.0
        elif self._seconds_moving <= 1.5:
            return 3.0
        elif self._seconds_moving <= 2.5:
            return 5.0
        else:
            return 6.0

    def update_position(self):
        """Update the ship's position based on the movement flag."""
        if self._moving_right and self.rect.right < self.screen_rect.right:
            self.x += self._delta_position()
        if self._moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self._delta_position()

        self.rect.x = self.x

    def move_right(self):
        """Sets moving right flag to true and starts timer."""
        self._start_time = time.perf_counter()
        self._moving_right = True

    def move_left(self):
        """Sets moving right flag to true and starts timer."""
        self._start_time = time.perf_counter()
        self._moving_left = True

    def stop_moving(self):
        """Sets moving right & left flags to false."""
        self._moving_left = False
        self._moving_right = False
