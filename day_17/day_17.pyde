# Day 17
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_17',
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
    pts = 150

    phase = random.random()*PI/2 + 3/4*PI
    vel1 = random.uniform(0.7, 2)
    vel2 = random.uniform(0.7, 4)
    for tt in range(pts):
        theta = TWO_PI/pts * tt

        x1 = side/3 + 100*cos(vel1*theta)
        y1 = side*1/4 + 40*sin(theta)
        x2 = side*2/3 + 150*cos(theta+phase)
        y2 = side*3/4 + 10*sin(vel2*theta+phase)
        line(x1, y1, x2, y2)

        # ellipse(width/2, height/2, side*0.8, side*0.8)
