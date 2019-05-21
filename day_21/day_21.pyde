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
# https://www.color-hex.com/color-palette/73465
colors = [
    color(240, 133, 133),
    color(255, 173, 152),
    color(255, 216, 156),
    color(159, 204, 173),
    color(65, 93, 133),
]


def draw_(seed=None):
    scale(1, -1)
    translate(0, -height)
    random.seed(seed)
    print 'seed', seed
    background(255)

    shapes = []
    shape_count = 15
    for idx in range(shape_count):
        f = idx / shape_count
        dy = (-0.2 + random.uniform(-1, 1)*0.05 + 1.4*f)*height
        amplitude = lerp(height/5, height/6, f)
        phase = lerp(1.8*PI, 0*PI, f)
        velocity = 1 - 0.4*(0.5 + 0.5 * (2*abs(f-0.5))**2)
        shape = [dy + amplitude * sin(velocity*x + phase)
                 for x in scaffold.distribute(0, TWO_PI, 100)]
        shapes.append((shape, random.choice(colors)))
    noStroke()
    for shape, clr in shapes[::-1]:
        fill(clr)
        draw_shape(shape)
    scaffold.hide_outside_circle()
