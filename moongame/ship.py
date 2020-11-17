import pyxel


class BaseShip:
    x = 0
    y = 0
    is_alive = True

    def __init__(self):
        self.x = pyxel.width // 2
        self.y = pyxel.height // 2

    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            img=0, u=0, v=0, w=7, h=7
        )

    def draw_start(self):
        pass

    def draw_ship_in_transition(self):
        pass


class NoobShip(BaseShip):
    pass
