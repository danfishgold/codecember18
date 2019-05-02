# Day 03
from __future__ import division
import os

base_filename = 'day_03'
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
                modifier = '_{}'.format(filename_description)
            else:
                modifier = ''
            filename = '{}_{:03d}{}.{}'.format(
                base_filename, index, modifier, extension)

            save(filename)
            print 'saved', filename
            filename_description = ''
        else:
            if key == BACKSPACE:
                filename_description = filename_description[:-1]
            else:
                filename_description = filename_description + key


def draw_circle(r, theta, length):
    circle(width/2 + r*cos(theta), height/2 + r*sin(theta), length)


side = 2000
minR = 0.003
maxR = 0.4
phi = (1+sqrt(5)) / 2
w = TWO_PI / phi
count = 1500


def setup():

    size(side, side)
    strokeWeight(side/800)
    background(255)

    for i in range(count):
        f = i / count
        # rdr/dt = const = > r = sqrt(c1 + c2t)
        r = side*sqrt(lerp(maxR*maxR, minR*minR, f))
        length = side/70*(1 - exp(-4*f))
        theta = w * i
        draw_circle(r, theta, length)

    save("../day_03.png")
    noLoop()


def draw():
    pass
