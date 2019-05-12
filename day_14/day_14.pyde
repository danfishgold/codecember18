# Day 14
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_14',
        extension='png'
    )


side = 500


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

    background(255)

    line_points = [(random.randint(0, side), 0)]
    is_vertical = True
    for _ in range(10):
        prev_x, prev_y = line_points[-1]
        if is_vertical:
            line_points.append((prev_x, random.randint(0, side)))
        else:
            line_points.append((random.randint(0, side), prev_y))
        is_vertical = not is_vertical

    for p1, p2 in zip(line_points, line_points[1:]):
        for weight, clr, cap in [(9, color(255), SQUARE), (5, color(255, 0, 0), PROJECT)]:
            stroke(clr)
            strokeWeight(weight)
            strokeCap(cap)
            noFill()
            line(p1[0], p1[1], p2[0], p2[1])
