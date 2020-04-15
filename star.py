import pygame
from random import choice
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the sky."""

    def __init__(self, ai_game):
        """Initialize the sky and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the root star image and set its rect attribute.
        self.image = pygame.image.load('img/star.png')
        self.rect_root = self.image.get_rect()

        # Load the random sized image and set its rect attribute.
        self.images = ('img/star_xs.png', 'img/star_xxs.png', 'img/star.png',)
        self.image = pygame.image.load(choice(self.images))
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)