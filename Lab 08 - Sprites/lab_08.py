""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.5
SPRITE_SCALING_MET = 0.5
COIN_COUNT = 50
MET_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Meteor(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 10,
                                         SCREEN_WIDTH + 300)

    def update(self):
        self.center_x -= 1

        if self.right < 0:
            self.reset_pos()


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.meteor_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)
        # Sound files comes from sound pack in kenney.nl
        self.coin_sound = arcade.load_sound("handleCoins2.ogg.")
        self.meteorhit_sound = arcade.load_sound("impactMetal_heavy_004.ogg")

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("playerShip3_red.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("star_gold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the coins
        for i in range(MET_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            meteor = Meteor("meteorBrown_big3.png", SPRITE_SCALING_MET)

            # Position the coin
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.meteor_list.append(meteor)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.meteor_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME OVER", 275, 275, arcade.color.WHITE, 40)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if len(self.coin_list) != 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.coin_list) > 0:
            self.meteor_list.update()
            self.coin_list.update()


        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.meteor_list)
        for meteor in hit_list:
            meteor.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.meteorhit_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
