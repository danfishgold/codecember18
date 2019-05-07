# Day 08
from __future__ import division
import os
import random

base_filename = 'day_08'
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


random.seed(1)

# https://coolors.co/29335c-ed7d3a-dee7e7-dee7e7-dee7e7
colors = [
    color(41, 51, 92),
    color(237, 125, 58),
    color(222, 231, 231)
]
side = 500
num_squares = 10
stroke_weight = 15
square_side = side / num_squares


def setup():
    size(side, side)
    background(255)
    stroke(0)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    strokeWeight(stroke_weight)
    stroke_middle = (stroke_weight // 4)*2+1

    for x in range(num_squares):
        for y in range(num_squares):
            stroke(random.choice(colors))
            rect(stroke_middle + x*square_side,
                 stroke_middle + y*square_side,
                 square_side - stroke_weight,
                 square_side - stroke_weight)
