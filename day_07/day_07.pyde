# Day 07
from __future__ import division
import os
import random

base_filename = 'day_07'
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


def is_point_ok(x, y, grid_side):
    inside_circle = sqrt(x**2 + y**2) < 0.4*grid_side
    even = (x+y) % 2 == 0
    return inside_circle and not even


random.seed(2)


side = 500
grid_scale = 11
grid_side = (side // grid_scale)//2 * 2 + 1
all_points = [(x, y)
              for x in range(-grid_side//2+1, grid_side//2+1)
              for y in range(-grid_side//2+1, grid_side//2+1)
              if is_point_ok(x, y, grid_side)]

# http://collection.mam.org/details.php?id=8007
red = color(183, 19, 0)
yellow = color(250, 209, 0)
blue = color(30, 63, 177)


def setup():
    size(side, side)
    strokeWeight(grid_scale)
    strokeCap(PROJECT)
    background(255)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():

    random.shuffle(all_points)
    for (x, y) in all_points[:floor(len(all_points)*1)]:
        stroke(random.choice([red, yellow, blue]))
        point(width/2 + grid_scale*x, height/2 + grid_scale*y)
