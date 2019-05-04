# Day 05
from __future__ import division
import os

base_filename = 'day_05'
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
            if indexes:
                index = max(indexes) + 1
            else:
                index = 1

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


def setup():
    size(side, side)
    strokeWeight(ceil(side/800))
    background(255)
    stroke(0)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():

    branch_count = 7
    n1 = 1
    n2 = n1
    point_count = 200
    radius = 0.4*side
    for branch in range(branch_count):
        phase = TWO_PI * branch/branch_count
        for vel in (TWO_PI*n1, -TWO_PI*n2):
            noFill()
            beginShape()
            for i in range(point_count+1):
                t = i / point_count
                r = pow(t, 4) * radius
                theta = vel*t + phase
                vertex(width/2+r*cos(theta), height/2+r*sin(theta))
            endShape()
