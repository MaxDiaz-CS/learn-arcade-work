import arcade

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
MOVEMENT_SPEED = 5


class Pacman:
    def __init__(self, center_x, center_y, change_x, change_y, width, height, color, start_angle, end_angle, tilt_angle,
                 num_segments):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.tilt_angle = tilt_angle
        self.num_segments = num_segments


    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_arc_filled(self.center_x,
                               self.center_y,
                               self.width,
                               self.height,
                               self.color,
                               self.start_angle,
                               self.end_angle,
                               self.tilt_angle,
                               self.num_segments)

    def update(self):
        # Move the ball
        self.center_y += self.change_y
        self.center_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.center_x < self.width:
            self.center_x = self.width

        if self.center_x > SCREEN_WIDTH - self.width:
            self.center_x = SCREEN_WIDTH - self.width

        if self.center_x < self.width:
            self.center_y = self.width

        if self.center_y > SCREEN_HEIGHT - self.width:
            self.center_y = SCREEN_HEIGHT - self.width

        if self.center_y < self.height:
            self.center_y = self.height

        if self.center_y > SCREEN_WIDTH - self.height:
            self.center_y = SCREEN_WIDTH - self.height

        if self.center_y < self.height:
            self.center_x = self.height

        if self.center_x > SCREEN_HEIGHT - self.height:
            self.center_x = SCREEN_HEIGHT - self.height


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        self.laser_sound = arcade.load_sound("pacman_chomp.wav")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Pacman(150, 144, 0, 0, 85, 86, arcade.color.YELLOW, 90, 360, 145, 54)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.center_x = x
        self.ball.center_y = y

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
            arcade.play_sound(self.laser_sound)
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
            arcade.play_sound(self.laser_sound)
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
            arcade.play_sound(self.laser_sound)
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
            arcade.play_sound(self.laser_sound)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(720, 720, "Pacman")
    arcade.run()


main()
