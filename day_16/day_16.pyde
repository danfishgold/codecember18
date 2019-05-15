# Day 16
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_16',
        extension='png'
    )


side = 1000


def ring(r1, r2, clr=color(0)):
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    diam = r1+r2
    ellipse(width/2, height/2, diam, diam)


def marc(r1, r2, theta1, theta2, clr=color(0)):
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    strokeCap(SQUARE)
    diam = r1+r2
    arc(width/2, height/2, diam, diam, theta1-0.005, theta2+0.005)


def dr(r, n):
    return r*PI/n


def rs(r, n, r_count=10):
    radiuses = [r]
    for _ in range(r_count-1):
        prev = radiuses[-1]
        radiuses.append(prev-dr(prev, n))
    return radiuses


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
    part_count = 26
    dtheta = TWO_PI/part_count
    background(255)
    noFill()

    rads = rs(side*0.4, part_count, 15)

    ring(rads[0], rads[1])
    ring(rads[4], rads[5])
    ring(rads[8], rads[9])

    for idx in range(part_count):
        marc(rads[1], rads[2], idx*dtheta, (idx+0.5)*dtheta)
        marc(rads[3], rads[4], (idx-0.5)*dtheta, idx*dtheta)
        if idx % 2 == 0:
            marc(rads[5], rads[7], idx*dtheta, (idx+0.5)*dtheta)
            marc(rads[6], rads[7], (idx+0.5)*dtheta, (idx+1.5)*dtheta)
        marc(rads[7], rads[8], idx*dtheta, (idx+0.5)*dtheta)
        marc(rads[9], rads[10], (idx-0.5)*dtheta, idx*dtheta)
