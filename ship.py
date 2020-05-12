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

        self.stop_moving()

        self.x = float(self.rect.x)

        self.center_ship()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def _delta_position(self):
        """Return ship speed."""
        return self.settings.ship_speed

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self._moving_right and self.rect.right < self.screen_rect.right:
            self.x += self._delta_position()
        elif self._moving_left and self.rect.left > 0:
            self.x -= self._delta_position()

        self.rect.x = int(self.x)

    def move_right(self):
        """Set moving right flag to true."""
        self._moving_right = True
        self._moving_left = False

    def move_left(self):
        """Set moving left flag to true."""
        self._moving_left = True
        self._moving_right = False

    def stop_moving(self):
        """Sets moving flags to false."""
        self._moving_left, self._moving_right = False, False

    def center_ship(self):
        """Center the ship on the screen."""
        self.stop_moving()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
