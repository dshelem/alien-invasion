import sys
from time import sleep
from random import randint
import atexit

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from button import Button
from game_over_badge import GameOverBadge
from mixer import Mixer


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)

        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

        self.sb = Scoreboard(self)

        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()
        self._create_stars()

        # Create the Play button and Game Over badge
        self.play_button = Button(self, "Play")
        self.game_over_badge = GameOverBadge(self, "Game Over")

        # Sounds and music mixer
        self.mixer = Mixer(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button_clicked(mouse_pos)

    def _check_play_button_clicked(self, mouse_pos):
        """Start a new game when the player clicks Play button."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """Restarts game."""
        # Reset the game statistics.
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.stats.game_over = False

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Update score and level.
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Start background music
        self.mixer.play_music()

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (self.stats.game_active and
                len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.mixer.stop_laser_shot()
            self.mixer.play_laser_shot()

    def _update_bullets(self):
        """Update bullets positions and get rid of the old bullets."""
        # Update bullets positions
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for key, values in collisions.items():
                for sprite in values:
                    self.stats.score += self.settings.alien_points

            self.mixer.stop_alien_crashed()
            self.mixer.play_alien_crashed()
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._level_up()

    def _level_up(self):
        """Fleet was destroyed: level up!"""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_game_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def save_high_score(self):
        """Saves high score on exit"""
        self.stats.save_high_score()

    def _update_aliens(self):
        """
        Check if the fleet is at the edge,
            then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        if self.stats.ships_left >= 2:
            # Decrement ships left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(self.settings.pause)
        else:
            # Game Over
            self.stats.game_active = False
            self.stats.game_over = True
            pygame.mouse.set_visible(True)
            self.play_button.draw_button()
            self.mixer.stop_music()
            self.mixer.play_game_over()
            self.stats.ships_left = 0
            self.sb.prep_ships()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - int(1.5 * alien_width)
        number_columns = available_space_x // int(1.8 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 3 * alien_height
                             - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for column_number in range(number_columns):
                self._create_alien(column_number, row_number)

    def _create_alien(self, column_number, row_number):
        """Create alien and place it on the screen."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * column_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop down the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_stars(self):
        """Create the stars in the sky."""
        # Create a star and find the number of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect_root.size
        available_space_x = self.settings.screen_width - int(2 * star_width)
        number_columns = available_space_x // int(1.8 * star_width)

        # Determine the number of rows of stars that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - int(2 * star_height)
                             - ship_height)
        number_rows = available_space_y // int(1.5 * star_height)

        # Create the full set of stars.
        for row_number in range(number_rows):
            for column_number in range(number_columns):
                self._create_star(column_number, row_number)

    def _create_star(self, column_number, row_number):
        """Create a star and place it on the screen."""
        star = Star(self)
        star_width, star_height = star.rect_root.size
        star.x = star_width + 2 * star_width * column_number + randint(-10, 10)
        star.rect.x = star.x
        star.y = star_height + 2 * star_height * row_number + randint(-10, 10)
        star.rect.y = star.y
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.aliens.draw(self.screen)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the score information.
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        if self.stats.game_over:
            self.game_over_badge.draw_badge()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right()
        elif event.key == pygame.K_LEFT:
            self.ship.move_left()
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif (event.key in (pygame.K_p, pygame.K_SPACE) and
              not self.stats.game_active):
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.ship.stop_moving()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = AlienInvasion()


    def at_exit_func():
        game.save_high_score()


    atexit.register(at_exit_func)
    game.run_game()
