import time
from gettext import gettext as _
import pyxel
from moongame.helper import *
from .helper import tick
from .core import physics, ship
from threading import Timer
import sched
import pymunk

s = sched.scheduler(time.time, time.sleep)

class BasicScene:

    next_scene = None
    start_time = 0
    static_objects = {}

    gravity = None  # type: physics.Gravity

    def __init__(self, game):
        self.game = game
        game.logger.debug(f'Changed scene: {self}')
        if self.gravity:
            self.space = pymunk.Space(threaded=True)  # ???
            self.space.gravity = self.gravity.grav_vector
            if self.player:
                print('player added', self.player.body)
                self.player.add_to_space(self.space)

        self.init()

    def init(self):
        pass

    @tick(0.1)
    def gravity_accel(self):
        self.player.velocity += self.gravity.ms2 * 0.1

    @property
    def player(self) -> ship.BaseShip:
        return self.game.player

    @property
    def time_passed(self):
        return time.time() - self.start_time

    def __repr__(self):
        return self.__class__.__name__

    def update(self):
        self.space.step(0.1 / 15)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(1, 1, f'Switched Scene: {self}', 1)


class StartScene(BasicScene):

    def update(self):
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.game.current_scene = Level1Scene(self.game)

    def draw(self):
        pyxel.cls(0)
        t = 'Probably moon travel'
        pyxel.text(center_x(t), self.game.s_height / 2, t, 4)
        t = 'by Pierre Geier / bloodywing'
        pyxel.text(center_x(t), self.game.s_height / 2 + pyxel.FONT_HEIGHT + 1, t, pyxel.frame_count % 10)

        t = _('PRESS [ENTER] key')
        pyxel.text(center_x(t), self.game.s_height / 2 + pyxel.FONT_HEIGHT*2 + 1, t, 10)


class Level1Scene(BasicScene):

    gravity = physics.EarthGravity()

    def init(self):
        ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        ground_body.position = (0, self.game.s_height)
        poly_ground = pymunk.Poly.create_box(ground_body, size=(self.game.s_width*2, 6), radius=5)
        print(poly_ground.body.position)
        self.static_objects['poly_ground'] = poly_ground  # type: pymunk.Poly
        self.space.add(self.static_objects['poly_ground'])

    def update(self):
        super(Level1Scene, self).update()
        self.player.update()
        #if self.player.y <= self.game.s_height:  # limit movement within the screen
        #    self.player.y += self.player.velocity // 2

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        pyxel.bltm(0, self.game.s_height - 8, 0, u=0, v=0, w=2*16, h=1)
        pyxel.text(0, 40, str(self.player.body.position), 1)
