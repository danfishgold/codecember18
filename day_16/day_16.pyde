# Day 16
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_16',
        extension='png'
    )


side = 1000


def ring(r1, r2, clr=color(0)):
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    diam = r1+r2
    ellipse(width/2, height/2, diam, diam)


def marc(r1, r2, theta1, theta2, clr=color(0)):
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    strokeCap(SQUARE)
    diam = r1+r2
    arc(width/2, height/2, diam, diam, theta1-0.005, theta2+0.005)


def dr(r, pixels):
    return r*TWO_PI/pixels


def rs(r, pixels, r_count=10):
    radiuses = [r]
    for _ in range(r_count-1):
        prev = radiuses[-1]
        radiuses.append(prev-dr(prev, pixels))
    return radiuses


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    draw_()
    noLoop()


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed
    copies = 14
    pixels_per_copy = 4
    pixel_count = pixels_per_copy*copies
    pattern = [
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1]
    ]
    dtheta = TWO_PI/pixel_count
    background(255)
    noFill()

    rads = rs(side*0.4, pixels=pixel_count, r_count=len(pattern)+1)

    for copy_index in range(copies):
        for row_index, row in enumerate(pattern):
            for col_index, col in enumerate(row):
                if col:
                    marc(
                        rads[row_index],
                        rads[row_index+1],
                        (copy_index*pixels_per_copy + col_index)*dtheta,
                        (copy_index*pixels_per_copy + col_index+1)*dtheta
                    )
