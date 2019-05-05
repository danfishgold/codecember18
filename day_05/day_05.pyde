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
    strokeWeight(ceil(side/500))
    background(255)
    stroke(0)


def mouseClicked():
    redraw()


t = 0


def draw():
    global t
    background(255)
    draw_(branch_count=7,
          n1=1,
          n2=-1,
          phase1=TWO_PI*t*(-0.1+0.03),
          phase2=TWO_PI*t*(0.1+0.03))
    t += 0.016


def draw_(branch_count, n1, n2, phase1, phase2):
    point_count = 200
    radius = 0.4*side
    noFill()
    for branch in range(branch_count):
        phase = TWO_PI * branch/branch_count
        for (n, time_phase) in [(n1, phase1), (n2, phase2)]:
            beginShape()
            for i in range(point_count+1):
                f = i / point_count
                r = pow(f, 4) * radius
                theta = TWO_PI*n*f + phase + time_phase
                vertex(width/2+r*cos(theta), height/2+r*sin(theta))
            endShape()
