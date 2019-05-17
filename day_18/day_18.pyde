# Day 18
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_18',
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


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)

    lines = [
        (
            random.choice([color(0), color(255)]),
            random.randint(5, 10)
        )
        for _ in range(100)]

    curr_x = 0
    for (clr, wd) in lines:
        fill(clr)
        noStroke()
        rect(curr_x, 0, wd, height)
        curr_x += wd
