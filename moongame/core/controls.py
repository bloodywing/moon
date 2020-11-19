import pyxel


class Control:

    move_up = None
    move_down = None
    move_left = None
    move_right = None

    """ 
            for k in pyxel.__dict__.keys():
            if k.startswith('KEY_'):
                if pyxel.btnp(getattr(pyxel, k)):
                    print(k)
    """

    def __init__(self):
        self.move_up = pyxel.KEY_W
        self.move_down = pyxel.KEY_S
        self.move_left = pyxel.KEY_A
        self.move_right = pyxel.KEY_D
        self.start_engine = pyxel.KEY_SPACE
