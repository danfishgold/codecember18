# Day 20: Dashes
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
        row_count=36
    )
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 2000

# # https://www.color-hex.com/color-palette/78339
# colors = [
#     color(228, 207, 249),
#     color(212, 223, 242),
#     color(246, 209, 224),
#     color(240, 175, 178),
#     color(249, 226, 197),
# ]

# # pastels on http://tools.medialab.sciences-po.fr/iwanthue/
# colors = [
#     color(214, 216, 180),
#     color(209, 187, 223),
#     color(170, 210, 191),
#     color(230, 184, 179),
#     color(163, 204, 226),
# ]

# # https://www.color-hex.com/color-palette/78363
# colors = [
#     color(255, 102, 153),
#     color(255, 140, 115),
#     color(255, 171, 84),
#     color(255, 209, 46),
#     color(255, 255, 0),
# ]


# https://www.color-hex.com/color-palette/78291
colors = [
    color(243, 229, 171),
    color(202, 215, 174),
    color(162, 202, 178),
    color(122, 188, 181),
    color(40, 161, 188),
][::-1]


def draw_(seed, row_count):
    random.seed(seed)
    print 'seed', seed
    background(255)
    padding = floor(0.8*side / row_count)
    stroke_weight = (side*0.9 / (2*row_count)) // 2 * 2 + 1
    min_width, max_width = 0, padding*2
    strokeWeight(stroke_weight)
    strokeCap(ROUND)
    for y in scaffold.distribute(0.1*side, 0.9*side, shift=padding):
        y = int(y)
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
                width = random_width(effective_max_width)
            pct = (x + width/2 - outer_padding) / (side - 2*outer_padding)
            stroke(random_color(colors, pct))
            line(x, y, x+width, y)
            x += width + padding


def random_color(colors, pct):
    pct += random.uniform(-1, 1)*0.3
    n = len(colors)
    idx = max(0, min(n-1, floor(pct*n)))
    return colors[idx]


def random_width(max_width):
    if random.random() < 0.15:
        return 0
    else:
        return random.randint(max_width//4, max_width)
