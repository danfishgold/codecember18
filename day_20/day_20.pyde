# Day 20
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_20',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(
        seed=seed,
        padding=side // 67,
        stroke_weight=(3 * side//500) // 2 * 2 + 1
    )
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 1000

# https://www.color-hex.com/color-palette/78339
colors = [
    color(228, 207, 249),
    color(212, 223, 242),
    color(246, 209, 224),
    color(240, 175, 178),
    color(249, 226, 197),
]


def draw_(seed, padding, stroke_weight):
    random.seed(seed)
    print 'seed', seed
    background(255)
    min_width, max_width = padding//3, padding*3
    strokeWeight(stroke_weight)
    strokeCap(ROUND)
    for y in scaffold.distribute(padding, side-padding, shift=padding):
        y = int(y)
        # outer_padding = padding*y//2
        if abs(y-side/2) > 0.4*side:
            continue
        outer_padding = floor(side/2 - sqrt((0.4*side)**2 - (y-side/2)**2))
        if side - 2*outer_padding <= min_width:
            continue
        x = outer_padding
        while x <= side - outer_padding - min_width:
            if side - outer_padding - x < max_width:
                width = side - outer_padding - x
            else:
                effective_max_width = min(
                    max_width,
                    side - outer_padding - min_width - padding - x
                )
                width = random.randint(min_width, effective_max_width)
            stroke(random.choice(colors))
            line(x, y, x+width, y)
            x += width + padding
