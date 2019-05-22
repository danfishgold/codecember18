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


triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))


def mouseClicked():
    global triangulation
    triangulation.add_point((mouseX/width, mouseY/height))
    redraw()


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 500


def draw_triangulation(triangulation):
    for (x1, y1), (x2, y2), (x3, y3) in triangulation.triangles():
        noStroke()
        fill(random.randint(0, 255))
        triangle(width*x1, height*y1, width*x2, height*y2, width*x3, height*y3)


def draw_(seed=None):
    random.seed(seed)
    print 'seed', seed
    background(255)
    draw_triangulation(triangulation)
