import unittest

from pygame.sprite import Group

from alien_invasion import AlienInvasion
from alien import Alien
from bullet import Bullet
from button import Button
from game_over_badge import GameOverBadge
from game_stats import GameStats
from mixer import Mixer
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from sound_button import SoundButton
from star import Star


class TestAlienClass(unittest.TestCase):
    """Testing Alien class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.alien = Alien(self.ai_game)

    def test_alien_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.alien.screen)

    def test_alien_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.alien.settings)

    def test_alien_image(self):
        """Test image is loaded."""
        self.assertIsNotNone(self.alien.image)

    def test_alien_rect_x(self):
        """Test alien rect.x value."""
        self.assertGreater(self.alien.rect.x, 0)

    def test_alien_rect_y(self):
        """Test alien rect.y value."""
        self.assertGreater(self.alien.rect.y, 0)

    def test_alien_x(self):
        """Test alien x value."""
        self.assertGreater(self.alien.x, 0)

    def test_alien_y(self):
        """Test alien y value."""
        self.assertGreater(self.alien.y, 0)

    def test_alien_check_edges(self):
        """Test check_edges function is working properly (1/3)."""
        self.assertFalse(self.alien.check_edges())

    def test_alien_check_edges_r(self):
        """Test check_edges function is working properly (2/3)."""
        self.alien.rect.right = self.ai_game.screen.get_rect().right
        self.assertTrue(self.alien.check_edges())

    def test_alien_check_edges_l(self):
        """Test check_edges function is working properly (3/3)."""
        self.alien.rect.left = 0
        self.assertTrue(self.alien.check_edges())

    def test_alien_update(self):
        """Test function that updates position of the alien."""
        x = self.alien.x + self.ai_game.settings.alien_speed * self.ai_game.settings.fleet_direction
        self.alien.update()
        self.assertEqual(x, self.alien.x)


class TestBulletClass(unittest.TestCase):
    """Testing Bullet class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.bullet = Bullet(self.ai_game)

    def test_bullet_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.bullet.screen)

    def test_bullet_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.bullet.settings)

    def test_bullet_image(self):
        """Test image is loaded."""
        self.assertIsNotNone(self.bullet.image)

    def test_bullet_rect_x(self):
        """Test bullet rect.x value."""
        self.assertGreater(self.bullet.rect.x, 0)

    def test_bullet_rect_y(self):
        """Test bullet rect.y value."""
        self.assertGreater(self.bullet.rect.y, 0)

    def test_bullet_y(self):
        """Test bullet y value."""
        self.assertGreater(self.bullet.y, 0)

    def test_bullet_update(self):
        """Test function that updates position of the bullet."""
        y = self.bullet.y - self.ai_game.settings.bullet_speed
        self.bullet.update()
        self.assertEqual(y, self.bullet.y)


class TestButtonClass(unittest.TestCase):
    """Testing Button class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.button = Button(self.ai_game, "Test Msg")

    def test_button_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.button.screen)

    def test_button_screen_rect(self):
        """Test screen_rect is present."""
        self.assertIsNotNone(self.button.screen_rect)

    def test_button_width(self):
        """Test width > 0."""
        self.assertGreater(self.button.width, 0)

    def test_button_height(self):
        """Test height > 0."""
        self.assertGreater(self.button.height, 0)

    def test_button_btn_color(self):
        """Test button color is set."""
        self.assertIs(type(self.button.button_color), tuple)

    def test_button_txt_color(self):
        """Test text color is set."""
        self.assertIs(type(self.button.text_color), tuple)

    def test_button_border_color(self):
        """Test border color is set."""
        self.assertIs(type(self.button.border_color), tuple)

    def test_button_border_width(self):
        """Test border width is not negative."""
        self.assertGreaterEqual(self.button.border_width, 0)

    def test_button_font(self):
        """Test font is present."""
        self.assertIsNotNone(self.button.font)

    def test_button_inner_rect(self):
        """Test inner_rect is present."""
        self.assertIsNotNone(self.button.inner_rect)

    def test_button_rect(self):
        """Test rect is present."""
        self.assertIsNotNone(self.button.rect)

    def test_button_msg_image(self):
        """Test msg_image is generated."""
        self.assertIsNotNone(self.button.msg_image)

    def test_button_msg_image_rect(self):
        """Test msg_image_rect is generated."""
        self.assertIsNotNone(self.button.msg_image_rect)


class TestGameOverBadgeClass(unittest.TestCase):
    """Testing GameOverBadge class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.game_over_badge = GameOverBadge(self.ai_game, "Test Msg")

    def test_game_over_badge_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.game_over_badge.screen)

    def test_game_over_badge_screen_rect(self):
        """Test screen_rect is present."""
        self.assertIsNotNone(self.game_over_badge.screen_rect)

    def test_game_over_badge_width(self):
        """Test width > 0."""
        self.assertGreater(self.game_over_badge.width, 0)

    def test_game_over_badge_height(self):
        """Test height > 0."""
        self.assertGreater(self.game_over_badge.height, 0)

    def test_game_over_badge_badge_color(self):
        """Test game over badge_color is set."""
        self.assertIs(type(self.game_over_badge.badge_color), tuple)

    def test_game_over_badge_txt_color(self):
        """Test text color is set."""
        self.assertIs(type(self.game_over_badge.text_color), tuple)

    def test_game_over_badge_border_color(self):
        """Test border color is set."""
        self.assertIs(type(self.game_over_badge.border_color), tuple)

    def test_game_over_badge_border_width(self):
        """Test border width is not negative."""
        self.assertGreaterEqual(self.game_over_badge.border_width, 0)

    def test_game_over_badge_font(self):
        """Test font is present."""
        self.assertIsNotNone(self.game_over_badge.font)

    def test_game_over_badge_inner_rect(self):
        """Test inner_rect is present."""
        self.assertIsNotNone(self.game_over_badge.inner_rect)

    def test_game_over_badge_rect(self):
        """Test rect is present."""
        self.assertIsNotNone(self.game_over_badge.rect)

    def test_game_over_badge_msg_image(self):
        """Test msg_image is generated."""
        self.assertIsNotNone(self.game_over_badge.msg_image)

    def test_game_over_badge_msg_image_rect(self):
        """Test msg_image_rect is generated."""
        self.assertIsNotNone(self.game_over_badge.msg_image_rect)


class TestGameStatsClass(unittest.TestCase):
    """Testing GameStats class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.game_stats = GameStats(self.ai_game)

    def test_game_stats_settings(self):
        """Checking settings is not None."""
        self.assertIsNotNone(self.game_stats.settings)

    def test_game_stats_ships_left(self):
        """Checking # of ships left initially."""
        self.assertEqual(self.game_stats.ships_left, self.game_stats.settings.ship_limit)

    def test_game_stats_score(self):
        """Checking score at the start if the game."""
        self.assertEqual(self.game_stats.score, 0)

    def test_game_stats_level(self):
        """Checking level at the start if the game."""
        self.assertEqual(self.game_stats.level, 1)

    def test_game_reset_stats(self):
        """Checking if reset stats function is working."""
        self.game_stats.ships_left = -1
        self.game_stats.score = 15000
        self.game_stats.level = 150
        self.game_stats.reset_stats()

        self.assertEqual(self.game_stats.ships_left, self.game_stats.settings.ship_limit)
        self.assertEqual(self.game_stats.score, 0)
        self.assertEqual(self.game_stats.level, 1)

    def test_game_stats_game_active_flag(self):
        """Checking status of the game active flag."""
        self.assertFalse(self.game_stats.game_active)

    def test_game_stats_game_over_flag(self):
        """Checking status of the game over flag."""
        self.assertFalse(self.game_stats.game_over)

    def test_game_stats_file_name(self):
        """Checking file_name is present."""
        self.assertIsNotNone(self.game_stats.file_name)


class TestMixerClass(unittest.TestCase):
    """Testing Mixer class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.mixer = Mixer(self.ai_game)

    def test_mixer_sound_on_off_flag(self):
        """Checking sound on/off flag is present."""
        self.assertIn(self.mixer.settings.sound_on, (True, False))

    def test_mixer_laser_shot_sound(self):
        """Checking laser shot is loaded."""
        self.assertIsNotNone(self.mixer.laser_shot)

    def test_mixer_alien_crashed_sound(self):
        """Checking alien crushed sound is loaded."""
        self.assertIsNotNone(self.mixer.alien_crashed)

    def test_mixer_game_over_sound(self):
        """Checking game over sound is loaded."""
        self.assertIsNotNone(self.mixer.game_over)


class TestScoreboardClass(unittest.TestCase):
    """Testing Scoreboard class."""
    def setUp(self):
        self.ai_game = AlienInvasion()
        self.score_board = Scoreboard(self.ai_game)

    def test_score_board_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.score_board.screen)

    def test_score_board_screen_rect(self):
        """Test screen_rect is present."""
        self.assertIsNotNone(self.score_board.screen_rect)

    def test_score_board_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.score_board.settings)

    def test_score_board_stats(self):
        """Test stats are present."""
        self.assertIsNotNone(self.score_board.stats)

    def test_score_board_text_color(self):
        """Test text color is set."""
        self.assertIs(type(self.score_board.text_color), tuple)

    def test_score_board_font(self):
        """Test font is present."""
        self.assertIsNotNone(self.score_board.font)

    def test_score_board_font_small(self):
        """Test font small is present."""
        self.assertIsNotNone(self.score_board.font_small)

    def test_score_board_high_score_text_color(self):
        """Test high score text color is set."""
        self.assertIs(type(self.score_board.high_score_text_color), tuple)

    def test_score_board_level_text_color(self):
        """Test level text color is set."""
        self.assertIs(type(self.score_board.level_text_color), tuple)

    def test_score_board_bg_color(self):
        """Test background color is set."""
        self.assertTrue(hasattr(self.score_board, 'bg_color'))

    def test_score_board_clock(self):
        """Test clock is set."""
        self.assertIsNotNone(self.score_board.clock)

    def test_score_board_score_image(self):
        """Test score image is set."""
        self.assertIsNotNone(self.score_board.score_image)

    def test_score_board_score_rect(self):
        """Test score rect is set."""
        self.assertIsNotNone(self.score_board.score_rect)

    def test_score_board_high_score_image(self):
        """Test high score image is set."""
        self.assertIsNotNone(self.score_board.high_score_image)

    def test_score_board_high_score_rect(self):
        """Test high score rect is set."""
        self.assertIsNotNone(self.score_board.high_score_image)

    def test_score_board_level_image(self):
        """Test level image is set."""
        self.assertIsNotNone(self.score_board.level_image)

    def test_score_board_level_rect(self):
        """Test level rect is set."""
        self.assertIsNotNone(self.score_board.level_rect)

    def test_score_board_fps_image(self):
        """Test fps image is set."""
        self.score_board.prep_fps()
        self.assertIsNotNone(self.score_board.fps_image)

    def test_score_board_fps_rect(self):
        """Test fps rect is set."""
        self.score_board.prep_fps()
        self.assertIsNotNone(self.score_board.fps_rect)

    def test_score_board_ships_class(self):
        """Test ships sprite group is set."""
        self.assertIsInstance(self.score_board.ships, Group)

    def test_score_board_ships_number(self):
        """Test ships number is properly set."""
        self.assertEqual(len(self.score_board.ships), self.score_board.stats.ships_left)

    def test_score_board_check_high_score(self):
        """Test check_high_score function works properly."""
        self.score_board.stats.score = self.score_board.stats.high_score + 10
        self.score_board.check_high_score()

        self.assertEqual(self.score_board.stats.score, self.score_board.stats.high_score)


class TestSettingsClass(unittest.TestCase):
    """Testing Settings class."""
    def setUp(self):
        self.settings = Settings()

    def test_settings_caption(self):
        """Checking caption attribute."""
        self.assertGreater(len(self.settings.caption), 0)

    def test_settings_screen_width(self):
        """Checking screen width attribute."""
        self.assertGreater(self.settings.screen_width, 0)

    def test_settings_screen_height(self):
        """Checking screen height attribute."""
        self.assertGreater(self.settings.screen_height, 0)

    def test_settings_bg_color(self):
        """Checking bg_color attribute."""
        self.assertIs(type(self.settings.bg_color), tuple)

    def test_settings_full_screen(self):
        """Checking full_screen attribute."""
        self.assertIn(self.settings.full_screen, (True, False))

    def test_settings_ship_limit(self):
        """Checking ship_limit attribute."""
        self.assertGreater(self.settings.ship_limit, 0)

    def test_settings_bullets_allowed(self):
        """Checking bullets_allowed attribute."""
        self.assertGreater(self.settings.bullets_allowed, 0)

    def test_settings_fleet_drop_speed(self):
        """Checking fleet_drop_speed attribute."""
        self.assertGreater(self.settings.fleet_drop_speed, 0)

    def test_settings_pause(self):
        """Checking pause attribute."""
        self.assertGreaterEqual(self.settings.pause, 0)

    def test_settings_speedup_scale(self):
        """Checking speedup_scale attribute."""
        self.assertGreater(self.settings.speedup_scale, 1.0)

    def test_settings_score_scale(self):
        """Checking score_scale attribute."""
        self.assertGreater(self.settings.score_scale, 1.0)

    def test_settings_music_volume(self):
        """Checking music_volume attribute."""
        self.assertGreaterEqual(self.settings.music_volume, 0.0)

    def test_settings_file_name(self):
        """Checking file_name attribute."""
        self.assertIsNotNone(self.settings.file_name)

    def test_settings_show_fps(self):
        """Checking show_fps attribute."""
        self.assertFalse(self.settings.show_fps)

    def test_settings_initialize_dynamic_settings(self):
        """Checking initialize_dynamic_settings() function works properly."""
        self.settings.ship_speed *= 2
        self.settings.bullet_speed *= 2
        self.settings.alien_speed *= 2
        self.settings.fleet_direction = -1
        self.settings.alien_points *= 2

        self.settings.initialize_dynamic_settings()

        self.assertEqual(self.settings.ship_speed, self.settings.SHIP_SPEED)
        self.assertEqual(self.settings.bullet_speed, self.settings.BULLET_SPEED)
        self.assertEqual(self.settings.alien_speed, self.settings.ALIEN_SPEED)
        self.assertEqual(self.settings.fleet_direction, 1)
        self.assertEqual(self.settings.alien_points, self.settings.ALIEN_POINTS)

    def test_settings_increase_game_speed(self):
        """Checking increase_game_speed() function works properly."""
        self.settings.initialize_dynamic_settings()
        self.settings.increase_game_speed()

        self.assertEqual(self.settings.SHIP_SPEED, self.settings.ship_speed / self.settings.speedup_scale)
        self.assertEqual(self.settings.BULLET_SPEED, self.settings.bullet_speed / self.settings.speedup_scale)
        self.assertEqual(self.settings.ALIEN_SPEED, self.settings.alien_speed / self.settings.speedup_scale)
        self.assertEqual(self.settings.ALIEN_POINTS, self.settings.alien_points / self.settings.score_scale)


class TestShipClass(unittest.TestCase):
    """Testing Ship class."""

    def setUp(self):
        self.ai_game = AlienInvasion()
        self.ship = Ship(self.ai_game)

    def test_ship_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.ship.screen)

    def test_ship_screen_rect(self):
        """Test screen_rect attribute is set."""
        self.assertIsNotNone(self.ship.screen_rect)

    def test_ship_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.ship.settings)

    def test_ship_image(self):
        """Test image is loaded."""
        self.assertIsNotNone(self.ship.image)

    def test_ship_rect_x(self):
        """Test ship rect.x value."""
        self.assertGreater(self.ship.rect.x, 0)

    def test_ship_rect_y(self):
        """Test ship rect.y value."""
        self.assertGreater(self.ship.rect.y, 0)

    def test_ship_x(self):
        """Test ship x value."""
        self.assertGreater(self.ship.x, 0)

    def test_ship_delta_position(self):
        """Test _delta_position function works properly."""
        self.assertEqual(self.ship._delta_position(), self.ship.settings.ship_speed)
        self.assertGreater(self.ship._delta_position(), 0)

    def test_ship_move_right(self):
        """Test move_right function works properly."""
        self.ship.move_left()
        self.ship.move_right()
        self.assertTrue(self.ship._moving_right)
        self.assertFalse(self.ship._moving_left)

    def test_ship_move_left(self):
        """Test move_left function works properly."""
        self.ship.move_right()
        self.ship.move_left()
        self.assertTrue(self.ship._moving_left)
        self.assertFalse(self.ship._moving_right)

    def test_ship_stop_moving(self):
        """Test stop_moving function works properly."""
        self.ship.move_left()
        self.ship.move_right()
        self.ship.stop_moving()
        self.assertFalse(self.ship._moving_left)
        self.assertFalse(self.ship._moving_right)

    def test_ship_update(self):
        """Test function that updates position of the ship."""
        x = self.ship.x
        self.ship.stop_moving()
        self.ship.update()
        self.assertEqual(x, self.ship.x)

        self.ship.move_right()
        self.ship.update()
        self.assertEqual(self.ship.x, x + self.ship._delta_position())

        self.ship.move_left()
        self.ship.update()
        self.assertEqual(self.ship.x, x)

        self.ship.stop_moving()

    def test_ship_center_ship(self):
        """Test function that centers the ship on the screen."""
        self.ship.move_right()
        self.ship.update()
        self.ship.update()
        self.assertNotEqual(self.ship.rect.midbottom, self.ship.screen_rect.midbottom)

        self.ship.center_ship()
        self.assertEqual(self.ship.rect.midbottom, self.ship.screen_rect.midbottom)

        self.ship.stop_moving()


class TestSoundButtonClass(unittest.TestCase):
    """Testing SoundButton class."""

    def setUp(self):
        self.ai_game = AlienInvasion()
        self.sound_button = SoundButton(self.ai_game)

    def test_sound_button_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.sound_button.settings)

    def test_sound_button_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.sound_button.screen)

    def test_sound_button_screen_rect(self):
        """Test screen_rect attribute is set."""
        self.assertIsNotNone(self.sound_button.screen_rect)

    def test_sound_button_image_sound_on(self):
        """Test image sound on is loaded."""
        self.assertIsNotNone(self.sound_button.image_sound_on)

    def test_sound_button_image_sound_off(self):
        """Test image sound off is loaded."""
        self.assertIsNotNone(self.sound_button.image_sound_off)

    def test_sound_button_rect_top(self):
        """Test sound_button rect.top value."""
        self.assertGreater(self.sound_button.rect.top, 0)

    def test_sound_button_rect_left(self):
        """Test sound_button rect.left value."""
        self.assertGreater(self.sound_button.rect.left, 0)


class TestStarClass(unittest.TestCase):
    """Testing Star class."""

    def setUp(self):
        self.ai_game = AlienInvasion()
        self.star = Star(self.ai_game)

    def test_star_screen(self):
        """Test screen is set."""
        self.assertIsNotNone(self.star.screen)

    def test_star_image(self):
        """Test image is loaded."""
        self.assertIsNotNone(self.star.image)

    def test_star_rect_x(self):
        """Test star rect.x value."""
        self.assertGreater(self.star.rect.x, 0)

    def test_star_rect_y(self):
        """Test star rect.y value."""
        self.assertGreater(self.star.rect.y, 0)

    def test_star_x(self):
        """Test star.x value."""
        self.assertGreater(self.star.x, 0)

    def test_star_y(self):
        """Test star.y value."""
        self.assertGreater(self.star.y, 0)


class TestAlienInvasionClass(unittest.TestCase):
    """Testing AlienInvasion class."""

    def setUp(self):
        self.ai_game = AlienInvasion()

    def test_alien_invasion_settings(self):
        """Test settings are present."""
        self.assertIsNotNone(self.ai_game.settings)

    def test_alien_invasion_stats(self):
        """Test statistics is present."""
        self.assertIsNotNone(self.ai_game.stats)

    def test_alien_invasion_screen(self):
        """Test screen is present."""
        self.assertIsNotNone(self.ai_game.screen)

    def test_alien_invasion_score_board(self):
        """Test score_board is present."""
        self.assertIsNotNone(self.ai_game.sb)

    def test_alien_invasion_ship(self):
        """Test ship class."""
        self.assertIs(type(self.ai_game.ship), Ship)

    def test_alien_invasion_bullets(self):
        """Test bullets class."""
        self.assertIs(type(self.ai_game.bullets), Group)

    def test_alien_invasion_aliens(self):
        """Test aliens class."""
        self.assertIs(type(self.ai_game.aliens), Group)

    def test_alien_invasion_stars(self):
        """Test stars class."""
        self.assertIs(type(self.ai_game.stars), Group)

    def test_alien_invasion_play_button(self):
        """Test play_button is present."""
        self.assertIsNotNone(self.ai_game.play_button)

    def test_alien_invasion_game_over_badge(self):
        """Test game_over_badge is present."""
        self.assertIsNotNone(self.ai_game.game_over_badge)

    def test_alien_invasion_mixer(self):
        """Test mixer is present."""
        self.assertIsNotNone(self.ai_game.mixer)

    def test_alien_sound_button(self):
        """Test sound button is present."""
        self.assertIsNotNone(self.ai_game.sound_button)


if __name__ == '__main__':
    unittest.main()
