# Day 17
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_17',
        extension='png'
    )


side = 500


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    draw_()
    noLoop()


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    phase0 = 0
    phase1 = random.uniform(2, TWO_PI)
    phase2 = random.uniform(2, TWO_PI)
    vel1 = random.uniform(0.5, 0.8)
    vel2 = random.uniform(0.5, 0.8)
    vel3 = random.uniform(0.7, 1.4)
    vel4 = random.uniform(0.7, 1.4)
    count = floor(100 * max([vel1, vel2]))

    background(255)
    stroke(0, 0, 0, 200)
    noFill()

    thetas = [TWO_PI*idx/count for idx in range(count)]
    pts1 = [
        (side/2 + side/4*cos(vel1*theta+phase0+phase1),
         side*1/4 + side/6*sin(vel2*theta+phase0+phase1))
        for theta in thetas
    ]

    pts2 = [
        (side/2 + side/4*cos(vel3*theta+phase0+phase2),
         side*3/4 + side/6*sin(vel4*theta+phase0+phase2))
        for theta in thetas
    ]
    for (x1, y1), (x2, y2) in zip(pts1, pts2):
        line(x1, y1, x2, y2)
        for pct in range(0, 100, 5):
            x = lerp(x1, x2, pct/100)
            y = lerp(y1, y2, pct/100)

    for shape in (pts1, pts2):
        beginShape()
        for x, y in shape:
            vertex(x, y)
        endShape()
