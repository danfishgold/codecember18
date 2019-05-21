# Day 21
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_21',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw_shape(ys):
    beginShape()
    dx = width / (len(ys)-1)

    vertex(width, 0)
    vertex(0, 0)
    for idx, y in enumerate(ys):
        vertex(idx*dx, y)
    endShape(CLOSE)


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 500


def draw_(seed=None):
    scale(1, -1)
    translate(0, -height)
    random.seed(seed)
    print 'seed', seed
    background(255)

    shapes = []
    shape_count = 10
    for idx in range(shape_count):
        f = idx / shape_count
        shape = [(-0.2 + 1.4*f)*height + height/6 * sin(x + scaffold.cubic_ease(f)*2*TWO_PI)
                 for x in scaffold.distribute(0, TWO_PI, 100)]
        shapes.append((shape, color(f*255)))
    noStroke()
    for shape, clr in shapes[::-1]:
        fill(clr)
        draw_shape(shape)
