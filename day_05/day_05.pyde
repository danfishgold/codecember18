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


side = 2000


def setup():
    size(side, side)
    smooth(8)
    strokeWeight(ceil(side/500))
    background(255)
    stroke(0)


def mouseClicked():
    global t
    t = 0


t = 0


def dv_and_t_final(di1, di2, branch_count, v0):
    # This calculation is in my notebook. It's complicated. But not very complicated
    return ((di1+di2)/(di1-di2)*v0,
            (di1-di2)/(2*branch_count*v0))


branch_count = 7
v0 = 0.175
(dv, t_final) = dv_and_t_final(2, -1, branch_count, v0)
time_steps = 50
dt = t_final / time_steps


def draw():
    global t
    if t < t_final:
        background(255)
        draw_(branch_count=branch_count,
              n1=1,
              n2=-1,
              phase1=TWO_PI*t*(-v0+dv),
              phase2=TWO_PI*t*(v0+dv))
        t += dt
        saveFrame('gif/{}_###.{}'.format(base_filename, extension))


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
