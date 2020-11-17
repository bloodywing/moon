import pyxel

def center_x(t: str):
    return pyxel.width / 2 - len(t) * 2

def center_y(t: str = None):
    return pyxel.height / 2 - pyxel.FONT_HEIGHT * 2
