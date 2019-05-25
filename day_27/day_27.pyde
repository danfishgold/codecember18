# Day 27
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_27',
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

# https://www.color-hex.com/color-palette/78648
colors = [
    color(230, 230, 250),
    color(211, 222, 229),
    color(192, 213, 208),
    color(173, 205, 187),
    color(153, 196, 167),
]


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    side_count = 15
    r = side / (side_count+1)
    xs = scaffold.distribute(0, width, side_count+2)[1:-1]
    ys = scaffold.distribute(0, height, side_count+2)[1:-1]
    noise_scale = 0.02 / (side / 500)
    noiseSeed(seed)
    for x in xs:
        for y in ys:
            shape = random.choice((0, 1, 2, 3))
            clr = random.choice(colors)
            fill(clr)
            stroke(clr)
            if shape == 0:
                circle(x, y, r)
            if shape == 1:
                square(x-r/2, y-r/2, r)
            if shape == 2:
                pts = [
                    (x-r/2, y-r/2),
                    (x+r/2, y-r/2),
                    (x-r/2, y+r/2),
                    (x+r/2, y+r/2),
                ]
                ignored_index = random.randint(0, 3)
                triangle = pts[:ignored_index] + pts[ignored_index+1:]
                beginShape()
                for pt in triangle:
                    vertex(*pt)
                endShape(CLOSE)
            if shape == 3:
                arcs = [
                    (x-r/2, y-r/2, 0, PI/2),
                    (x+r/2, y-r/2, PI/2, PI),
                    (x+r/2, y+r/2, PI, 3*PI/2),
                    (x-r/2, y+r/2, 3*PI/2, 2*PI),
                ]
                xc, yc, theta1, theta2 = random.choice(arcs)
                arc(xc, yc, 2*r, 2*r, theta1, theta2)
