import os
import logging
import importlib
from .scenes import *
from .core.controls import Control
from .core.generics import AbstractAppObject, App
from .helper import game_path, palette
from moongame.core.ship import *

WIDTH = 256
HEIGHT = 256


class Game(AbstractAppObject):

    debug = False
    current_scene = None
    s_scale = 1
    player = None  # type: BaseShip

    def __init__(self, args):
        self.debug = args.debug
        self.s_scale = args.scale
        App.set_game_instance(self)

        # controls, just a class now
        # todo make it possible to set own controls
        self.control = Control()
        # DEBUGGING STUFF
        logging.basicConfig(filename='moon.log', filemode='w')
        self.logger = logging.getLogger(__name__)  # type: logging.Logger
        if self.debug:
            self.logger.setLevel(logging.DEBUG)

        # set screen size, scale and fullscreen or not
        pyxel.init(height=HEIGHT, width=WIDTH, caption='Moon',
                   palette=palette('default'),
                   fullscreen=args.fullscreen, scale=args.scale, fps=60)
        # Scene
        self.player = NoobShip()
        self.current_scene = StartScene(self)
        if self.debug and args.scene:
            self.current_scene = self.get_scene(args.scene)(self)

        pyxel.load(os.path.join(game_path, 'assets', 'base.pyxres'))
        self.logger.debug(f'Pyxel: {pyxel.VERSION}')
        self.logger.debug('Moon started')
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
        pyxel.text(0, 0, f'Velocity: {int(self.player.velocity)}', pyxel.COLOR_WHITE)
        pyxel.text(0, 10, f'Engine Power: {int(self.player.impulse)}', pyxel.COLOR_WHITE)
        pyxel.text(0, 20, f'Distance: {int(self.player.distance)}', pyxel.COLOR_WHITE)

    def get_scene(self, name):
        scenes = importlib.import_module('moongame.scenes')
        return getattr(scenes, name)
