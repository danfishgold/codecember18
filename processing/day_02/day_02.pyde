# Day 02: Julia
# Inspired by drawings of my high school friend, Julia.
from __future__ import division


def draw_triangle(r, theta, length):
    resetMatrix()
    translate(width/2 + r*cos(theta), height/2 + r*sin(theta))
    rotate(theta - HALF_PI)
    fill(255)
    stroke(255)
    triangle(-length/2, 0, 0, length, length/2, 0)
    stroke(0)
    line(-length/2, 0, 0, length)
    line(length/2, 0, 0, length)


side = 2000
minR = 0.003
maxR = 0.4
phi = (1+sqrt(5)) / 2
w = TWO_PI / phi
count = 1200


def setup():

    size(side, side)
    strokeWeight(side/800)
    background(255)

    for i in range(count):
        f = i / count
        # rdr/dt = const = > r = sqrt(c1 + c2t)
        r = side*sqrt(lerp(maxR*maxR, minR*minR, f))
        length = lerp(side/90, side/70, f)
        theta = w * i
        draw_triangle(r, theta, length)

    save("../day_02.png")
    noLoop()


def draw():
    pass
