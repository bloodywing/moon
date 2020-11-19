from functools import wraps
from typing import Callable, Optional, Any, Iterable, Mapping
import os
import pyxel
import threading
from time import sleep

game_path = os.path.dirname(os.path.abspath(__file__))

def center_x(t: str):
    return pyxel.width / 2 - len(t) * 2


def center_y(t: str = None):
    return pyxel.height / 2 - pyxel.FONT_HEIGHT * 2


def worker(e: threading.Event, tick_seconds: float):
    while True:
        e.set()
        sleep(tick_seconds)

class tick:
    def __init__(self, tick_seconds):
        self.tick_seconds = tick_seconds

        e = threading.Event()
        self.e = e
        t = threading.Thread(target=worker, args=(e, tick_seconds))
        t.setDaemon(True)
        t.start()

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            if self.e.is_set():
                thread = threading.Thread(target=func, args=args)
                thread.start()
                self.e.clear()
        return wrapper


def palette(palette_name: str):
    palette = []
    with open(os.path.join(game_path, 'assets', 'palettes', palette_name)) as fp:
        for h_code in fp:
            palette.append(int(h_code, 16))
    return palette

