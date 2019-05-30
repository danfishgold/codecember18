# Day 01: Air Conditioner
# It looks like an air conditioning tube...
# Inspired by the example here:
# https:#processing.org/tutorials/gettingstarted/
from __future__ import division

# Size
side = 2000

# Time and space
t = 0
t1 = 10000  # movement with t^0.25 zoom
t2 = t1 + 100  # movement with t^1 zoom
dt = 0.1  # the minimum time difference to add
minDist = side/180  # the minimum distance between consecutive circle centers

# Parameters
randomSeed(4)
# Velocities
centerRW = random(0.025, 0.029)*PI  # 0.027
centerW = random(0.008, 0.012)*PI  # 0.01
radiusW = random(0.019, 0.023)*PI  # 0.021
shiftXW = random(0.0016, 0.0020)*PI  # 0.0018
shiftYW = random(0.0026, 0.0030)*PI  # 0.0028
# Phases
centerRP = random(0, 2)*PI
centerP = random(0, 2)*PI
radiusP = random(0, 2)*PI
shiftXP = random(0, 2)*PI
shiftYP = random(0, 2)*PI


def setup():
    global t, prevDx, prevDy

    size(side, side)
    fill(255)
    background(255)
    strokeWeight(ceil(side/700))

    prevDx = dx(0)
    prevDy = dy(0)
    newDx = prevDx
    newDy = prevDy

    while t < t2:
        # while the new circle is too close to the previous one
        while dist(prevDx, prevDy, newDx, newDy) < minDist:
            # increase t and try again
            t += dt
            fac = factor(t)
            newDx = fac*dx(t)
            newDy = fac*dy(t)
        step(t)
        prevDx = newDx
        prevDy = newDy
    save("../day_01.png")
    noLoop()


def centerR(t):
    return 0.18*side + 0.04*side*sin(t*centerRW + centerRP)


def shiftR(t):
    return 0.12*side


def dx(t):
    centerX = centerR(t) * cos(t*centerW + centerP)
    shiftX = shiftR(t) * cos(t*shiftXW + shiftXP)
    return centerX + shiftX


def dy(t):
    centerY = centerR(t) * sin(t*centerW + centerP)
    shiftY = shiftR(t) * sin(t*shiftYW + shiftYP)
    return centerY + shiftY


def radius(t):
    return 0.14*side + 0.02*side*cos(t*radiusW + radiusP)


def factor(t):
    f = (t2 - t) / t2
    if t < t1:
        return pow(f, 0.25)
    else:
        return pow((t2-t1) / t2, 0.25) * (t2-t) / (t2-t1)


def step(t):
    r = radius(t)
    f = factor(t)
    ellipse(width/2 + f*dx(t), height/2 + f*dy(t), r, r)


def draw():
    global t, prevDx, prevDy
    newDx, newDy = prevDx, prevDy
    if t < t2:
        # while the new circle is too close to the previous one
        while dist(prevDx, prevDy, newDx, newDy) < minDist:
            # increase t and try again
            t += dt
            fac = factor(t)
            newDx = fac*dx(t)
            newDy = fac*dy(t)
        step(t)
        prevDx = newDx
        prevDy = newDy
