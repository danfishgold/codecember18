# Day 27 but not really
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='grid_stuff',
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
    side_count = 20
    r = side / (side_count+1)
    xs = scaffold.distribute(0, width, side_count+2)[1:-1]
    ys = scaffold.distribute(0, height, side_count+2)[1:-1]
    noise_scale = 0.02 / (side / 500)
    noiseSeed(seed)
    for x in xs:
        for y in ys:
            val = noise(noise_scale*x, noise_scale*y)
            # if 0 <= val <= 0.33:
            #     shape = 0
            # elif 0.66 <= val <= 1:
            #     shape = 1
            # else:
            #     shape = 2
            shape = random.choice((2, 3, 6))

            if shape == 0:
                strokeWeight(3/sqrt(2))
                line(x-r/2, y-r/2, x+r/2, y+r/2)
                line(x+r/2, y-r/2, x-r/2, y+r/2)
            if shape == 1:
                strokeWeight(3)
                line(x-r/2, y, x+r/2, y)
                line(x, y-r/2, x, y+r/2)
            if shape == 2:
                strokeWeight(3)
                line(x-r/4, y-r/4, x+r/4, y-r/4)
                line(x+r/4, y-r/4, x+r/4, y+r/4)
                line(x-r/4, y-r/4, x-r/4, y+r/4)
                line(x-r/4, y+r/4, x+r/4, y+r/4)

            if shape == 3:
                strokeWeight(3)
                line(x-r/2, y-r/2, x+r/2, y-r/2)
                line(x+r/2, y-r/2, x+r/2, y+r/2)
                line(x-r/2, y-r/2, x-r/2, y+r/2)
                line(x-r/2, y+r/2, x+r/2, y+r/2)
            if shape == 4:
                circle(x, y, r)
