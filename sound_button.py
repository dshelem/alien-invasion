import pygame
from pygame.sprite import Sprite


class SoundButton(Sprite):
    """A class for sound on/off button in the game."""

    def __init__(self, ai_game):
        """Initialize the button and set its starting position."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the button image and set its rect attribute.
        self.image_sound_on = pygame.image.load('img/sound_on.png')
        self.image_sound_off = pygame.image.load('img/sound_off.png')
        self.rect = self.image_sound_on.get_rect()

        # Set button's starting position.
        self.rect.top = 25
        self.rect.left = 350

    def draw_sound_button(self):
        """Draw the button to the screen depending on sound-on flag."""
        if self.settings.sound_on:
            self.screen.blit(self.image_sound_on, self.rect)
        else:
            self.screen.blit(self.image_sound_off, self.rect)
