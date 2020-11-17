import argparse
from ctypes import cdll
from gettext import gettext as _
from moongame.game import Game

# This is a hack to help pyinstaller detecting the sdl2 library
cdll.LoadLibrary('libSDL2_image-2.0.so.0')


if __name__ == '__main__':
    parse = argparse.ArgumentParser(prog='Probably moon travel')
    parse.add_argument('-f', '--fullscreen', action='store_true', default=False, help=_('Start the game in fullscreen'))
    parse.add_argument('-s', '--scale', default=2, type=int, help=_('Set scaling for the game'))
    parse.add_argument('-d', '--debug', default=False, action='store_true', help=_('Enable debugging'))
    args = parse.parse_args()
    Game(args)
