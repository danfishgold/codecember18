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
random.seed(1)


def random_pattern():
    clr = color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        100
    )
    step = random.randint(5, 15)
    offset = random.randint(0, step-1)
    return (clr, step, offset)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    patterns = [random_pattern() for _ in range(10)]

    background(255)
    for clr, step, offset in patterns:
        for x in range(offset, n, step):
            for y in range(offset, n, step):
                pixel(x, y, clr)
