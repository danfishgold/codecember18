# Day 11: Blokus
from __future__ import division
import scaffold


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


side = 500
square_count = 20
square_side = side/square_count

square1 = {(0, 0)}
square2 = {(0, 0), (1, 0), (0, 1), (1, 1)}
line2 = {(0, 0), (0, 1)}
line3 = {(0, 0), (0, 1), (0, 2)}
line4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
line5 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
corner22 = {(0, 0), (1, 0), (0, 1)}
corner23 = {(0, 0), (1, 0), (0, 1), (0, 2)}
corner24 = {(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)}
corner33 = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
plus23 = {(0, 0), (0, 1), (0, 2), (1, 1)}
plus33 = {(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}

shapes = [square1, square2,
          line2, line3, line4, line5,
          corner22, corner23, corner24, corner33,
          plus23, plus33]


def rotate(shape, n, new_origin=(0, 0)):
    x0, y0 = new_origin
    if n == 0:
        def rotator(x, y): return (x, y)
    elif n == 1:
        def rotator(x, y): return (y, -x)
    elif n == 2:
        def rotator(x, y): return (-x, -y)
    elif n == 3:
        def rotator(x, y): return (-y, x)

    return {rotator(x-x0, y-y0) for (x, y) in shape}


def shift(shape, x0, y0):
    return {(x0+x, y0+y) for (x, y) in shape}


def corners(shape, dirs):
    shifts = [shift(shape, *sh)
              for (dx, dy) in dirs
              for sh in [(dx, 0), (0, dy)]
              ]
    shifted = set.union(*shifts)
    return shape.difference(shifted)


def draw_shape(shape, color):
    fill(color)
    for (x, y) in shape:
        rect(x*square_side, y*square_side, square_side, square_side)


def draw_board():
    strokeWeight(side // 500 // 2 * 2 + 1)
    stroke(0)
    for rowcol in range(square_count+1):
        line(0, square_side*rowcol, side, square_side*rowcol)
        line(square_side*rowcol, 0, square_side*rowcol, side)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    draw_board()
    for index, shape in enumerate(shapes):
        draw_shape(shift(shape,
                         2 + 4*(index % 4),
                         2 + 6*(index // 4)),
                   color(0, 255, 0))
