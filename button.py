import pygame.font

class Button:
    """Class for creating buttons in the game."""

    def __init__(self, ai_game, msg):
        """Init button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (133, 255, 192)
        self.text_color = (255, 255, 255)
        self.border_color = (255, 255, 255)
        self.border_width = 5
        self.font = pygame.font.SysFont(None, 48)

        # Build inner rectangle for border effect
        self.inner_rect = pygame.Rect(0, 0, self.width - 2 * self.border_width,
                                 self.height - 2 * self.border_width)
        self.inner_rect.center = self.screen_rect.center

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                    self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button and then draw message."""
        self.screen.fill(self.border_color, self.rect)
        self.screen.fill(self.button_color, self.inner_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)