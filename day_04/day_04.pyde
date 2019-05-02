# Day 04
from __future__ import division
import os

base_filename = 'day_04'
extension = 'png'
filename_description = ''

phi = (1 + sqrt(5)) / 2


def keyPressed():
    global filename_description
    if isinstance(key, unicode):
        if key == '\n':
            files = os.listdir('.')
            matches = [
                match(f, r'{}_(\d+).*\.{}'.format(base_filename, extension)) for f in files]
            indexes = [int(m[1]) for m in matches if m is not None]
            index = max(indexes) + 1

            if filename_description:
                modifier = '_{}'.format(filename_description.replace(' ', '_'))
            else:
                modifier = ''
            filename = '{}_{:02d}{}.{}'.format(
                base_filename, index, modifier, extension)

            save(filename)
            print 'saved', filename
            filename_description = ''
        else:
            if key == BACKSPACE:
                filename_description = filename_description[:-1]
            else:
                filename_description = filename_description + key


side = 1000


def balloon_petal(theta, length, width):
    pushMatrix()
    rotate(theta)
    wd = 1.6*width
    ht = 1.3*length
    bezier(0, 0, -wd, ht, wd, ht, 0, 0)
    popMatrix()


def ellipse_petal(theta, length, width):
    pushMatrix()
    rotate(theta)
    ellipse(0, length/2, width, length)
    popMatrix()


def flower_petals(petal, length, width, count):
    if count > 20:
        dtheta = TWO_PI/phi
    else:
        dtheta = TWO_PI/count
    theta = 0
    for i in range(count):
        petal(theta, length, width)
        theta += dtheta


def flower(petal, length, width, center_radius, count):
    fill(255, 120, 20)
    stroke(0)
    flower_petals(petal, length, width, count)
    ellipse(0, 0, center_radius, center_radius)


def setup():

    size(side, side)
    strokeWeight(ceil(side/800))
    background(255)
    stroke(0)

    translate(width/2, height/2)
    flower(balloon_petal, length=100, width=40, center_radius=20, count=21)

    noLoop()


def draw():
    pass
