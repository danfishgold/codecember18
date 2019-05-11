# Day 13
from __future__ import division
import scaffold
import random
import collections


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_13',
        extension='png'
    )


side = 500
noise_scale = 0.02


def draw_array(array):
    for (x, y), val in array.items():
        stroke(255*val)
        point(x, y)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    array = {(x, y): noise(noise_scale*x, noise_scale*y)
             for y in range(side)
             for x in range(side)}
    draw_array(array)
