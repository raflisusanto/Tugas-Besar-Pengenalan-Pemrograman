# settings -> Ukuran layar, warna
class Settings:
    """A Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 960
        self.bg_color = "black"  # r, g, b

        # Ship Settings
        self.ship_speed = 1.6
        self.ship_limit = 5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_allowed = 4

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 15
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Inisialisasi kecepatan game
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.5

        # Fleet direction of 1 represents right, -1 represents left.
        self.fleet_direction = -1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and aliens point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)