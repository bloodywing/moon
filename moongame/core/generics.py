import pymunk

class AbstractAppObject:
    @property
    def game(self):
        return App._instance


class App:
    _instance = None

    @classmethod
    def set_game_instance(cls, o):
        cls._instance = o

    @classmethod
    def get_instance(cls):
        return cls._instance


class MoveAbleObject(AbstractAppObject):

    u = 0
    v = 0
    _x = 0
    _y = 0
    w = 7
    h = 7
    _velocity = 0
    mass = 10

    def __init__(self):
        self.body = pymunk.Body(self.mass, moment=pymunk.moment_for_box(self.mass, (self.w, self.h)))
        self.body.position = self.x, self.y
        self.poly = pymunk.Poly.create_box(self.body, size=(self.w*2, self.h*2))
        print(self.poly.body)

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.poly)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, v):
        self._velocity = v if self.distance > 0 or self.impulse > 0 else 0

    @property
    def distance(self):
        return abs(self.y - self.game.s_height + self.h)

    def flip(self, d=None):

        if d == 'up':
            self.w = abs(self.w)
            self.h = abs(self.h)
        elif d == 'down':
            self.w = abs(self.w) * -1
            self.h = abs(self.h) * -1
        else:
            self.w *= -1
            self.h *= -1

    def m_up(self, d: int):
        self.y -= d

    def m_down(self, d: int):
        self.y += d

    def m_left(self, d: int):
        self.x -= d

    def m_right(self, d: int):
        self.x += d
