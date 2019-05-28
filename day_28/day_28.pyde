# Day 28
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_28',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 500


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    line_count = random.randint(5, 20)
    center_count = random.randint(2, 5)
    print line_count, center_count
    center_radius_fraction = 0.5
    center_phase = 0  # random.uniform(0, TWO_PI)
    for center_idx in range(center_count):
        theta = TWO_PI * center_idx/center_count + center_phase

        def angle(a): return a - asin(center_radius_fraction*sin(a - theta))
        for line_idx in range(line_count):
            theta1 = angle(TWO_PI * line_idx/line_count + theta)
            theta2 = angle(TWO_PI * line_idx/line_count + PI + theta)
            x1, y1 = 0.4*side*cos(theta1), 0.4*side*sin(theta1)
            x2, y2 = 0.4*side*cos(theta2), 0.4*side*sin(theta2)
            line(side/2 + x1, side/2 + y1, side/2 + x2, side/2 + y2)
