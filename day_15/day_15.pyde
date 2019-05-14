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
tile_size = 15
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
    return (clr, offset_x, offset_y)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    patterns = [random_pattern(tile_size) for _ in range(60)]

    background(255)
    for clr, offset_x, offset_y in patterns:
        for x0 in range(0, n, tile_size):
            for y0 in range(0, n, tile_size):
                pixel(x0+offset_x, y0+offset_y, clr)
                pixel(x0+tile_size-offset_x, y0+tile_size-offset_y, clr)
