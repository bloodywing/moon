import os
import pyxel
import logging
from gettext import gettext as _
from .scenes import *
from .ship import *

WIDTH = 256
HEIGHT = 256

game_path = os.path.dirname(os.path.abspath(__file__))


class Game:

    debug = False
    current_scene = None
    s_scale = 1
    player = None  # type: BaseShip

    def __init__(self, args):
        self.debug = args.debug
        self.s_scale = args.scale
        # DEBUGGING STUFF
        logging.basicConfig(filename='moon.log')
        self.logger = logging.getLogger(__name__)  # type: logging.Logger
        if self.debug:
            self.logger.setLevel(logging.DEBUG)

        # set screen size, scale and fullscreen or not
        pyxel.init(height=HEIGHT, width=WIDTH, fullscreen=args.fullscreen, scale=args.scale, fps=16)
        self.logger.debug('Moon started')

        self.current_scene = StartScene(self)

        pyxel.load(os.path.join(game_path, 'assets', 'base.pyxres'))
        self.player = NoobShip()
        pyxel.run(self.update, self.draw)

    @property
    def s_width(self):
        return pyxel.width

    @property
    def s_height(self):
        return pyxel.height

    def update(self):
        self.current_scene.update()

    def draw(self):
        self.current_scene.draw()
