# Day 30
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_30',
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
seed = 4092  # random.randint(1, 10000)

side = 2000


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    circle_count = 5
    point_count = 400
    min_rad_factor = 0.4
    max_rad_factor = 0.9
    outer_radius = 0.4*side
    circles = []
    for _ in range(circle_count):
        theta = random.uniform(0, TWO_PI)
        r = random.uniform(min_rad_factor, max_rad_factor)*outer_radius
        x, y = r*cos(theta), r*sin(theta)
        rad = outer_radius - r
        phase = random.uniform(0, TWO_PI)
        circles.append((side/2 + x, side/2 + y, rad, phase))

    noStroke()
    fill(0, 0, 0, 3)
    for point_idx in range(point_count):
        theta = TWO_PI * point_idx / point_count
        translate(side/2, side/2)
        rotate(TWO_PI/point_count)
        translate(-side/2, -side/2)
        beginShape()
        for xc, yc, r, phase in circles:
            vertex(
                xc + r*cos(theta+phase),
                yc + r*sin(theta+phase)
            )
        endShape(CLOSE)
