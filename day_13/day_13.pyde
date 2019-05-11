# Day 13
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_13',
        extension='png'
    )


side = 500
noise_scale = 0.02


def draw_array(array, array_side):
    for x in range(array_side):
        for y in range(array_side):
            stroke(255*array[x][y])
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
    array = [[noise(noise_scale*x, noise_scale*y)
              for y in range(side)]
             for x in range(side)]
    draw_array(array, side)
