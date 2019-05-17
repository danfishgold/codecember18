# Day ##
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_##',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


random.seed(1)


def draw():
    seed = random.randint(1, 10000)
    draw_(seed)
    noLoop()


side = 500


def draw_(seed=None):
    random.seed(seed)
    print 'seed', seed
    background(255)
    ellipse(width/2, height/2, side*0.8, side*0.8)
