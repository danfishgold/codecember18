# Day 03: Circles
# Like yesterday, but with a few cool improvements
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


def draw_circle(r, theta, length):
    circle(width/2 + r*cos(theta), height/2 + r*sin(theta), length)


side = 2000
minR = 0
maxR = 0.4
phi = (1+sqrt(5)) / 2
batches = 5
w = TWO_PI / phi / batches
count = 800
power = 5


def setup():

    size(side, side)
    strokeWeight(ceil(side/800))
    background(255)

    for batch in range(batches):
        draw_points(count/batches, TWO_PI*batch/batches, power)
    noLoop()


def draw_points(count, phase, power):
    for i in range(ceil(count)):
        f = i / count
        # rdr/dt = const = > r = sqrt(c1 + c2t)
        r = side*pow(lerp(pow(maxR, power), pow(minR, power), f), 1/power)
        length = side/70*(1 - exp(-4*f))
        theta = w * i + phase
        draw_circle(r, theta, length)


def draw():
    pass
