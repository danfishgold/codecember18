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
    line_count = 150
    order = range(line_count)
    random.shuffle(order)
    for idx in range(line_count):
        i1 = order[idx-1]
        i2 = order[idx]
        theta1 = TWO_PI * i1 / line_count
        theta2 = TWO_PI * i2 / line_count
        x1, y1 = 0.4*side*cos(theta1), 0.4*side*sin(theta1)
        x2, y2 = 0.4*side*cos(theta2), 0.4*side*sin(theta2)
        dtheta = min((theta1-theta2) % TWO_PI, (theta2-theta1) % TWO_PI)
        rmin_over_r = cos(dtheta/2)
        stroke(255-rmin_over_r * 255)
        line(side/2 + x1, side/2 + y1, side/2 + x2, side/2 + y2)
