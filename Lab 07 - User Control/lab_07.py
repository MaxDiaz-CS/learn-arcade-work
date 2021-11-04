import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 850
MOVEMENT_SPEED = 8


class Clouds:
    def __init__(self, position_x, position_y, change_x, change_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        x = self.position_x
        y = self.position_y

        arcade.draw_circle_filled(400 + x - 200, 540 + y - 400, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(340 + x - 200, 470 + y - 400, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(340 + x - 200, 440 + y - 400, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(310 + x - 200, 530 + y - 400, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(230 + x - 200, 450 + y - 400, 60, arcade.color.WHITE)

    def update(self):
        # Move the pacman
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the pacman hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class Pacman:
    def __init__(self, center_x, center_y, change_x, change_y, width, height, color, start_angle, end_angle, tilt_angle,
                 num_segments):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.error_sound = arcade.load_sound("impactMetal_heavy_000.ogg")
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
        """ Draw the pacmans with the instance variables we have. """
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
        # Move the pacman
        self.center_y += self.change_y
        self.center_x += self.change_x

        # See if the pacman hit the edge of the screen. If so, change direction
        if self.center_x < self.width:
            self.center_x = self.width
            arcade.play_sound(self.error_sound)
        if self.center_x > SCREEN_WIDTH - self.width:
            self.center_x = SCREEN_WIDTH - self.width
            arcade.play_sound(self.error_sound)
        if self.center_x < self.width:
            self.center_y = self.width
            arcade.play_sound(self.error_sound)
        if self.center_y > SCREEN_HEIGHT - self.width:
            self.center_y = SCREEN_HEIGHT - self.width
            arcade.play_sound(self.error_sound)
        if self.center_y < self.height:
            self.center_y = self.height
            arcade.play_sound(self.error_sound)
        if self.center_y > SCREEN_WIDTH - self.height:
            self.center_y = SCREEN_WIDTH - self.height
            arcade.play_sound(self.error_sound)
        if self.center_y < self.height:
            self.center_x = self.height
            arcade.play_sound(self.error_sound)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Load the sound when the game starts
        self.laser_sound = arcade.load_sound("impactBell_heavy_001.ogg")
        self.error_sound = arcade.load_sound("impactMetal_heavy_000.ogg")

        self.set_mouse_visible(False)

        # creating the pacman
        self.cloud = Clouds(300, 300, 0, 0, 15)
        self.pacman = Pacman(150, 144, 0, 0, 85, 86, arcade.color.YELLOW, 90, 360, 145, 54)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 800, 150, 1, arcade.csscolor.DIM_GRAY)

        # Colosseum
        arcade.draw_lrtb_rectangle_filled(100, 400, 325, 150, arcade.csscolor.NAVAJO_WHITE)
        arcade.draw_ellipse_filled(390, 238, 52, 179,
                                   arcade.color.NAVAJO_WHITE, 180)
        arcade.draw_ellipse_filled(110, 238, 52, 179,
                                   arcade.color.NAVAJO_WHITE, 180)
        # Top Windows of the Colosseum
        arcade.draw_arc_filled(400, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(370, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(340, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(310, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(280, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(250, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(220, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(190, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(160, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(130, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(100, 280, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)

        # Top Windows of the Colosseum
        arcade.draw_arc_filled(400, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(370, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(340, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(310, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(280, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(250, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(220, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(190, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(160, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(130, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(100, 250, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)

        # Top Windows of the Colosseum
        arcade.draw_arc_filled(400, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(370, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(340, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(310, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(280, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(250, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(220, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(190, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(160, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(130, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(100, 220, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)

        # Top Windows of the Colosseum
        arcade.draw_arc_filled(400, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(370, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(340, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(310, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(280, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(250, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(220, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(190, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(160, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(130, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)
        arcade.draw_arc_filled(100, 190, 20, 40,
                               arcade.color.BLACK, 0, 180, 0)

        # flags poles
        arcade.draw_line(100, 325, 100, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(130, 325, 130, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(160, 325, 160, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(190, 325, 190, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(220, 325, 220, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(250, 325, 250, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(250, 325, 250, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(280, 325, 280, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(310, 325, 310, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(340, 325, 340, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(370, 325, 370, 345, arcade.color.WOOD_BROWN, 4)
        arcade.draw_line(400, 325, 400, 345, arcade.color.WOOD_BROWN, 4)

        # flags
        arcade.draw_lrtb_rectangle_filled(100, 117, 345, 335, arcade.csscolor.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(130, 147, 345, 335, arcade.csscolor.GOLDENROD)
        arcade.draw_lrtb_rectangle_filled(160, 177, 345, 335, arcade.csscolor.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(190, 207, 345, 335, arcade.csscolor.GOLDENROD)
        arcade.draw_lrtb_rectangle_filled(220, 237, 345, 335, arcade.csscolor.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(250, 267, 345, 335, arcade.csscolor.GOLDENROD)
        arcade.draw_lrtb_rectangle_filled(280, 297, 345, 335, arcade.csscolor.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(310, 327, 345, 335, arcade.csscolor.GOLDENROD)
        arcade.draw_lrtb_rectangle_filled(340, 357, 345, 335, arcade.csscolor.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(370, 387, 345, 335, arcade.csscolor.GOLDENROD)
        arcade.draw_lrtb_rectangle_filled(400, 417, 345, 335, arcade.csscolor.DARK_RED)

        # Doors
        arcade.draw_lrtb_rectangle_filled(120, 137, 165, 149, arcade.csscolor.BEIGE)
        arcade.draw_lrtb_rectangle_filled(137, 154, 165, 149, arcade.csscolor.BEIGE)

        arcade.draw_lrtb_rectangle_filled(220, 237, 165, 149, arcade.csscolor.BEIGE)
        arcade.draw_lrtb_rectangle_filled(237, 254, 165, 149, arcade.csscolor.BEIGE)

        arcade.draw_lrtb_rectangle_filled(330, 347, 165, 149, arcade.csscolor.BEIGE)
        arcade.draw_lrtb_rectangle_filled(347, 364, 165, 149, arcade.csscolor.BEIGE)

        arcade.draw_rectangle_filled(550, 180, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(550, 230, 60, 80, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(450, 180, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(450, 230, 60, 80, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(50, 180, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(50, 230, 60, 80, arcade.csscolor.DARK_GREEN)
        self.cloud.draw()
        self.pacman.draw()

    def update(self, delta_time):
        self.cloud.update()
        self.pacman.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.cloud.position_x = x
        self.cloud.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.pacman.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.pacman.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.pacman.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.pacman.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.pacman.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.pacman.change_y = 0


def main():
    MyGame(640, 480, "Lab 7")
    arcade.run()


main()
