# Day 12
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_12',
        extension='png'
    )


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


side = 500


def setup():
    size(side, side)


random.seed(1)


def draw_():
    noiseSeed(random.randint(1, 10000))
    noise_scale = 0.02
    noiseDetail(4, 0.5)

    # ellipse(width/2, height/2, side*0.8, side*0.8)
    for x in range(0, side):
        for y in range(0, side):
            noise_value = noise(x * noise_scale, y * noise_scale)
            stroke(255*noise_value)
            point(x, y)
