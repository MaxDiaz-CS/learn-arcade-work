"""
Sprite move between different rooms.
If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""
import arcade
import os
import random

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
NUMBER_OF_COINS = 30
SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Test"

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.coin_list = arcade.SpriteList()
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    # Walls for the interior of the box
    for y in range(600, 600, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(100, 200, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 350
        room.wall_list.append(wall)

    for y in range(0, 200, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 150
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 275
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(680, 500, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 275
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(320, 500, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(300, 425, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for y in range(96, 196, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(90, 250, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 525
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(600, 600, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 525
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(400, 650, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 450
        room.wall_list.append(wall)

    for y in range(275, 350, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 675
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(725, 850, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 225
        room.wall_list.append(wall)

    for y in range(0, 150, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 760
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(205, 600, 50):
        wall = arcade.Sprite("bedrock.png", SPRITE_SCALING)
        wall.center_x = 720
        wall.center_y = y
        room.wall_list.append(wall)

    # Load the background image for this level.
    room.background = arcade.load_texture("landscape.jpg")

    # If you want coins or monsters in a level, then add that code here.
    for i in range(NUMBER_OF_COINS):
        #
        coin = arcade.Sprite("star_gold.png", SPRITE_SCALING_COIN)

        # --- IMPORTANT PART ---

        # Boolean variable if we successfully placed the coin
        coin_placed_successfully = False

        # Keep trying until success
        while not coin_placed_successfully:
            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(coin, room.wall_list)

            # See if the coin is hitting another coin
            coin_hit_list = arcade.check_for_collision_with_list(coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                # It is!
                coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(coin)

        # --- END OF IMPORTANT PART ---

    return room





class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Other Sprite variables
        self.coin_list = None
        self.score = 0
        self.wall_list = None

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.coin_sound = arcade.load_sound("coin.ogg")

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("playerShip3_red.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()
        self.rooms[self.current_room].coin_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.coin_list.update()
        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0

            self.player_sprite.center_x = SCREEN_WIDTH

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].coin_list)

        for hit in hit_list:
            hit.remove_from_sprite_lists()
            arcade.play_sound(self.coin_sound)
            self.score += 1


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()