import pyxel
import pymunk
from .generics import MoveAbleObject


class BaseShip(MoveAbleObject):
    """
    TODO: make the ship move
    TODO: Ship rotation - fuck no support for that in pyxel
    """
    is_alive = True
    _velocity = 0
    impulse = 0
    mass = 100
    _x = 0
    _y = 0
    engine_power = 10

    # PyMunk Physics
    body = None  # type: pymunk.Body
    poly = None  # type: pymunk.Poly

    def __init__(self):
        self.x = pyxel.width // 2
        self.y = pyxel.height // 2
        super().__init__()

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            img=0, u=self.u, v=self.v, w=self.w, h=self.h
        )

    def update(self):

        self.velocity = self.body.velocity[1]
        self.x, self.y = self.body.position

        if pyxel.btnp(self.game.control.start_engine, 1, 3):
            self.impulse += 120
            self.body.apply_impulse_at_local_point((0, self.impulse *-1))

        if pyxel.btn(self.game.control.move_left):
            self.body.apply_impulse_at_local_point((-100, 0))

        if pyxel.btn(self.game.control.move_right):
            self.body.apply_impulse_at_local_point((100, 0))

        if pyxel.btnr(self.game.control.start_engine):
            self.body.apply_impulse_at_local_point((0, self.impulse))

        if not pyxel.btn(self.game.control.start_engine):
            self.impulse = 0

    def draw_start(self):
        pass

    def draw_ship_in_transition(self):
        pass


class NoobShip(BaseShip):
    pass
