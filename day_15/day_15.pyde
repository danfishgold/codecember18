# Day 15
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_15',
        extension='png'
    )


def pixel(x, y, clr):
    fill(clr)
    noStroke()
    return square(x*scale, y*scale, scale)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    draw_()
    noLoop()


side = 500
n = 100
scale = side//(n-1)
tile_size = n//5
random.seed(1)


def random_pattern(tile_size):
    clr = color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        100
    )
    offset_x = random.randint(0, tile_size-1)
    offset_y = random.randint(0, tile_size-1)

    symmetry = 8
    return (clr, offset_x, offset_y, symmetry)


def copies(x, y, s, symmetry=8):
    if symmetry == 8:
        return ((x, y), (s-x, y), (x, s-y), (s-x, s-y),
                (y, x), (s-y, x), (y, s-x), (s-y, s-x)
                )
    if symmetry == 4:
        return ((x, y), (s-x, y), (x, s-y), (s-x, s-y))
    if symmetry == 2:
        return ((x, y), (s-x, s-y))


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    patterns = [random_pattern(tile_size) for _ in range(tile_size*3)]

    background(255)
    for clr, offset_x, offset_y, symmetry in patterns:
        for x0 in range(0, n, tile_size):
            for y0 in range(0, n, tile_size):
                for dx, dy in copies(offset_x, offset_y, tile_size, symmetry=symmetry):
                    pixel(x0+dx, y0+dy, clr)
