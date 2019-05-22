# Day 22
from __future__ import division
import scaffold
import random
from delaunay import Triangulation


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_22',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed, 50, 20)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 500


# https://www.color-hex.com/color-palette/78498
colors = [
    color(66, 42, 87),
    color(89, 72, 110),
    color(112, 101, 133),
    color(158, 161, 179),
    color(181, 190, 202),
]


def draw_triangulation(triangulation):
    for (x1, y1), (x2, y2), (x3, y3) in triangulation.triangles():
        clr = random.choice(colors)
        stroke(clr)
        fill(clr)
        triangle(width*x1, height*y1, width*x2, height*y2, width*x3, height*y3)


triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))


def draw_(seed, point_count, perimiter_count):
    global triangulation
    random.seed(seed)
    print 'seed', seed
    background(255)
    triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))

    for idx in range(perimiter_count):
        theta = idx / perimiter_count * TWO_PI
        x, y = 0.5 + 0.4*cos(theta), 0.5 + 0.4*sin(theta)
        triangulation.add_point((x, y))

    for _ in range(point_count):
        x, y = 1, 1
        while (x-0.5)**2 + (y-0.5)**2 > 0.4**2:
            x, y = random.uniform(0, 1), random.uniform(0, 1)
        triangulation.add_point((x, y))
    draw_triangulation(triangulation)
