"""
Singleton class for AI Game testing.

Since setUp function is called for every test method,
we are creating all required objects only once.
"""

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


class _AIGameSingleton:

    def __init__(self) -> None:
        self.ai_game = AlienInvasion()
        self.alien = Alien(self.ai_game)
        self.bullet = Bullet(self.ai_game)
        self.button = Button(self.ai_game, "Test Msg")
        self.game_over_badge = GameOverBadge(self.ai_game, "Test Msg")
        self.game_stats = GameStats(self.ai_game)
        self.mixer = Mixer(self.ai_game)
        self.score_board = Scoreboard(self.ai_game)
        self.settings = Settings()
        self.ship = Ship(self.ai_game)
        self.sound_button = SoundButton(self.ai_game)
        self.star = Star(self.ai_game)


ai_sng = _AIGameSingleton()
