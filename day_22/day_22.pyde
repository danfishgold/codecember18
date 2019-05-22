# Day 22
from __future__ import division
import scaffold
import random
from delaunay import Triangulation
import poisson_disc


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
    draw_(seed, point_distance=0.1)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 2000


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
        clr = lerpColor(colors[0], colors[-1], random.uniform(0, 1))
        stroke(255)
        strokeWeight(side // 500 // 2 * 2 + 1)
        fill(clr)
        triangle(width*x1, height*y1, width*x2, height*y2, width*x3, height*y3)


triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))


def draw_(seed, point_distance):
    global triangulation
    random.seed(seed)
    print 'seed', seed
    background(255)
    triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))

    theta = acos(1 - point_distance**2 / (2*0.4*0.4))
    perimiter_count = floor(TWO_PI/theta)

    perimiter = []
    for idx in range(perimiter_count):
        theta = idx / perimiter_count * TWO_PI
        x, y = 0.5 + 0.4*cos(theta), 0.5 + 0.4*sin(theta)
        perimiter.append((x, y))

    for (x, y) in poisson_disc.sample(initial_set=perimiter, r=point_distance):
        triangulation.add_point((x, y))
    draw_triangulation(triangulation)
