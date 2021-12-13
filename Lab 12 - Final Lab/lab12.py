import arcade
import arcade
import random
import os

PLATFORM_SCALING = 0.5
SCALE = 0.5
SPRITE_SCALING = 0.5
TILE_SCALING = 0.5
GRID_PIXEL_SIZE = 128
SPRITE_SIZE = int(GRID_PIXEL_SIZE * SPRITE_SCALING)
GRAVITY = 0.25
SPAWN_X = 200
SPAWN_Y = 150
WIDTH = 1000
HEIGHT = 650
SCREEN_TITLE = "Side-Scroller Game"
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7
JUMP_SPEED = 10

SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 50



class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        """ This should set up your game and get it ready to play """
        # Replace 'pass' with the code to set up your game
        pass

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.SPACE:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)


class GameOverView(arcade.View):
    """ Class to manage the game over view """
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        if key == arcade.key.ESCAPE:
            menu_view = MenuView()
            self.window.show_view(menu_view)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.enemy_list = None
        self.plants_list = None
        self.coin_list = None
        # Set up the player
        self.player_sprite = None
        self.score = 0
        self.lives = None
        self.coin_sound = None
        self.error_sound = None
        # Physics engine
        self.physics_engine = None
        self.game_over = False

        # Used for scrolling map
        self.view_left = 0
        self.view_bottom = 0

        # Track what keys are pressed
        self.left_pressed = False
        self.right_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(WIDTH, HEIGHT)
        self.camera_gui = arcade.Camera(WIDTH, HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.plants_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coin_sound = arcade.load_sound("coin1.wav")
        self.error_sound = arcade.load_sound("error4.wav")

        self.score = 0
        self.lives = 3

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.4)
        # Starting position of the player
        self.player_sprite.center_x = SPAWN_X
        self.player_sprite.center_y = SPAWN_Y
        self.player_list.append(self.player_sprite)

        # -- Draw a enemy on the platfoRM
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 325
        enemy.left = 400

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 800
        enemy.boundary_left = 300
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 120
        enemy.left = 1100

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 1200
        enemy.boundary_left = 700
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 120
        enemy.left = 1100

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 1400
        enemy.boundary_left = 700
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # The lava Section
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 220
        enemy.left = 1900

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 2100
        enemy.boundary_left = 1700
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 220
        enemy.left = 1400

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 1600
        enemy.boundary_left = 1200
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 220
        enemy.left = 1600

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 1800
        enemy.boundary_left = 1400
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        enemy.bottom = 220
        enemy.left = 2300

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 2500
        enemy.boundary_left = 2100
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 260
        enemy.left = 2600

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 2800
        enemy.boundary_left = 2400
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 290
        enemy.left = 2800

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 3000
        enemy.boundary_left = 2600
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 260
        enemy.left = 3100

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 3300
        enemy.boundary_left = 2900
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 200
        enemy.left = 3400

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 3600
        enemy.boundary_left = 2900
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 250
        enemy.left = 3900

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 4200
        enemy.boundary_left = 3700
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 250
        enemy.left = 4200

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 4500
        enemy.boundary_left = 4000
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 250
        enemy.left = 4500

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 4800
        enemy.boundary_left = 4300
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 280
        enemy.left = 4700

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 5000
        enemy.boundary_left = 4500
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 190
        enemy.left = 4900

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 5200
        enemy.boundary_left = 4700
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)
        enemy.bottom = 210
        enemy.left = 5200

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = 5500
        enemy.boundary_left = 5000
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        coordinate_list_coin = [[2480, 180],
                                [2725, 210],
                                [2900, 275],
                                [3090, 210],
                                [3190, 165],
                                [3350, 80],
                                [3450, 80],
                                [1410, 180],
                                [1650, 180],
                                [1860, 180],
                                [2060, 180],
                                [2280, 180],
                                [1150, 175],
                                [500, 180],
                                [700, 180],
                                [285, 225],
                                [650, 400],
                                [325, 100],
                                [625, 134],
                                [3550, 80],
                                [3650, 80],
                                [3845, 80],
                                [3950, 80],
                                [4050, 80],
                                [4150, 80],
                                [4250, 80],
                                [4350, 80],
                                [4500, 80],
                                [4600, 180],
                                [4700, 200],
                                [4800, 200],
                                [4900, 200],
                                [5000, 200],
                                [5100, 180],
                                [5200, 80],
                                [5400, 140],
                                [5500, 200],
                                [5575, 350]
                                ]

        for coordinate in coordinate_list_coin:
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = coordinate[0]
            coin.center_y = coordinate[1]
            # Add the coin to the lists
            self.coin_list.append(coin)

        # --- Load our map
        # Read in the tiled map
        map_name = "mariolevel1.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)

        # Set wall and coin SpriteLists
        # Any other layers here. Array index must be a layer.
        self.wall_list = self.tile_map.sprite_lists["Walls"]
        self.plants_list = self.tile_map.sprite_lists["Plants"]

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            self.wall_list,
            gravity_constant=GRAVITY
        )

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()
        self.coin_list.draw()
        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.plants_list.draw()
        self.enemy_list.draw()

        arcade.draw_text(f"Score: {self.score}", self.view_left + 20, self.view_bottom + 60, arcade.color.WHITE, 24)
        arcade.draw_text(f"Lives: {self.lives}", self.view_left + 20, self.view_bottom + 30, arcade.color.WHITE, 24)

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME OVER", 275, 275, arcade.color.WHITE, 40)

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        if not self.game_over:
            # Move the enemies
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                # If the enemy hit the left boundary, reverse
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

            # See if the player hit a worm. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = False

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        # self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        # Generate a list of all sprites that collided with the player.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)
        if self.score >= 37:
            self.game_over = True
        arcade.draw_text("GAME OVER", 275, 275, arcade.color.WHITE, 40)

        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.enemy_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for enemy in enemy_hit_list:
            enemy.remove_from_sprite_lists()
            self.lives -= 1
            arcade.play_sound(self.error_sound)
        if self.lives < 1:
            self.game_over = True
        arcade.draw_text("GAME OVER", 300, 275, arcade.color.WHITE, 40)

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a
        smoother pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()



def main():
    """ Startup """
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Minimal Example")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()