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
    # if (x*scale-side/2)**2 + (y*scale-side/2)**2 > (0.4*side)**2:
    #     return
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


def random_pattern_part(tile_size):
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


def random_pattern(tile_size, pattern_count):
    pattern = [random_pattern_part(tile_size) for _ in range(pattern_count)]
    pixels = []
    for clr, offset_x, offset_y, symmetry in pattern:
        for x, y in copies(offset_x, offset_y, tile_size, symmetry=symmetry):
            pixels.append((x, y, clr))
    return pixels


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

    background(255)
    for x0 in range(0, n, tile_size):
        for y0 in range(0, n, tile_size):
            for dx, dy, clr in random_pattern(tile_size, pattern_count=2*tile_size):
                pixel(x0+dx, y0+dy, clr)
