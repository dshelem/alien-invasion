import pygame.font
from pygame.sprite import Group
import pygame.time

from ship import Ship

class Scoreboard:
    """A class to display scoring information."""

    def __init__(self, ai_game):
        """Init scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 16)
        self.high_score_text_color = (255, 255, 255)
        self.level_text_color = (255, 255, 255 )

        # self.bg_color = (255, 255, 255)
        self.bg_color = None

        # Prepare the initial score, level and left ships images.
        self.prep_images()

        # Clock
        self.clock = pygame.time.Clock()

    def prep_images(self):
        """Prepare images for scoreboard"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + \
                    "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.bg_color)

        # Display the score at the top center of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.high_score_text_color, self.bg_color)

        # Display the high score at the top right corner of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True,
            self.level_text_color, self.bg_color)

        # Display level below high score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.high_score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_fps(self):
        """Prep fps to display"""
        # Update clock. get_fps() wouldn't work without it
        self.clock.tick()
        fps_str = f"FPS: {int(self.clock.get_fps())}"
        self.fps_image = self.font_small.render(fps_str, True,
            self.text_color, self.bg_color)

        # Display FPS in bottom left corner
        self.fps_rect = self.fps_image.get_rect()
        self.fps_rect.left = 20
        self.fps_rect.bottom = self.screen_rect.bottom - 20

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            # Create extra small ships for score board
            ship = Ship(self.ai_game, True)
            ship.rect.top = 20
            ship.rect.left = 20 + ship_number * ship.rect.width
            ship.rect.left += ship_number * 10

            self.ships.add(ship)

    def show_score(self):
        """Draw scores. level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def show_fps(self):
        """Draw FPS"""
        self.screen.blit(self.fps_image, self.fps_rect)


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()