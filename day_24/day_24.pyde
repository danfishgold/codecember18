# Day 24: Mountains
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_24',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed, line_count=100, line_length=500)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 2000


def draw_line(ys, y0):
    n = len(ys)
    beginShape()
    vertex(0, height)
    for idx in range(n):
        x = width * idx / (n-1)
        vertex(x, height*(y0 + ys[idx]))
    vertex(width, height)
    endShape(CLOSE)


def draw_(seed, line_count, line_length):
    noise_scale = 5
    noiseSeed(seed)
    noiseDetail(4, 0.4)
    random.seed(seed)
    print 'seed', seed
    background(255)

    def wrapper(x):
        return (1-2*abs(x-0.5))**0.5

    strokeWeight(side//500)

    lines = []
    for y0 in scaffold.distribute(0, 1, line_count+2)[1:-1]:
        ys = [-0.05-0.4*wrapper(x)*(noise(noise_scale*x, noise_scale*y0)-0.5)
              for x in scaffold.distribute(0, 1, count=line_length)]
        lines.append(ys)
        fill(255)
        stroke(0)
        draw_line(ys, y0)

    scaffold.hide_outside_circle()
