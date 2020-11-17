from gettext import gettext as _
import pyxel
from moongame.helper import *

class BasicScene:

    next_scene = None

    def __init__(self, game):
        self.game = game
        game.logger.debug(f'Changed scene: {self}')

    @property
    def player(self):
        return self.game.player

    def __repr__(self):
        return self.__class__.__name__

    def update(self):
        pass

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

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
