# Day 04
from __future__ import division
import os

base_filename = 'day_04'
extension = 'png'
filename_description = ''


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


def ellipse_petal(theta, length, width):
    pushMatrix()
    rotate(theta)
    ellipse(0, length/2, width, length)
    popMatrix()

def flower_petals(petal, length, width, count):
    for i in range(count):
        petal(TWO_PI*i/count, length, width)

def flower(petal, length, width, center_radius, count):
    fill(255, 120, 20)
    stroke(0)
    ellipse(0, 0, center_radius, center_radius)
    flower_petals(petal, length, width, count)
    noStroke()
    fill(255, 120, 20)
    ellipse(0, 0, center_radius, center_radius)


def setup():

    size(side, side)
    strokeWeight(ceil(side/800))
    background(255)
    stroke(0)

    translate(width/2, height/2)
    flower(ellipse_petal, 100, 10, 20, 21)

    noLoop()


def draw():
    pass
