import sys
from random import randint
from time import sleep

import pygame

from settings import Settings
from ship_SW import Ship
from bullet_SW import Bullet
from alien_SW import Alien
from game_stats import GameStats


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)

        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _create_fleet(self):
        """Creates fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Calculate space for vertical placement of aliens with two margins
        #   equal to alien height at the top and bottom
        available_space_y = self.settings.screen_height - 2 * alien_height
        # Calc number of rows
        number_of_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_of_rows):
            self._create_alien(row_number)

    def _create_alien(self, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Introducing randomness
        alien.x = self.settings.screen_width - 2 * alien_width + randint(-30, 30)
        alien.y = alien_height + 2 * alien_height * row_number + randint(-30, 30)

        alien.rect.x = alien.x
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (self.stats.game_active and len(self.bullets)
                < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullets positions and get rid of the old bullets."""
        # Update bullets positions.
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update aliens on the screen"""
        self._check_aliens_edge()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._reset_game()

    def _check_aliens_edge(self):
        """Check if any of aliens crossed left border of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._reset_game()
                break

    def _reset_game(self):
        """Ship lost - reset game"""
        if self.stats.ships_left >= 1:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self.ship.center_ship()
            self._create_fleet()

            sleep(self.settings.pause)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.ship.move_up()
        elif event.key == pygame.K_DOWN:
            self.ship.move_down()
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.ship.stop_moving()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = AlienInvasion()
    game.run_game()