import argparse
import platform
from ctypes import cdll
from gettext import gettext as _
from moongame.game import Game
import pymunk
import os

if platform.system() == 'Linux':
    # This is a hack to help pyinstaller detecting the sdl2 library
    cdll.LoadLibrary('libSDL2_image-2.0.so.0')
cdll.LoadLibrary(pymunk.chipmunk_path)

if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='Probably moon travel')
    parse.add_argument('-f', '--fullscreen', action='store_true', default=False, help=_('Start the game in fullscreen'))
    parse.add_argument('-s', '--scale', default=2, type=int, help=_('Set scaling for the game'))
    parse.add_argument('-d', '--debug', default=False, action='store_true', help=_('Enable debugging'))
    parse.add_argument('--scene', default=None, type=str)
    args = parse.parse_args()
    Game(args)
