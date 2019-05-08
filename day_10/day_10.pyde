# Day 10: Tsuro
from __future__ import division
import os

base_filename = 'day_10'
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


def tile(xc, yc, tile_side, line):
    third = tile_side/3
    x0, y0 = xc - tile_side/2, yc - tile_side/2
    tile_side = 100
    stroke(0)
    strokeWeight(2)
    noFill()
    rect(x0, y0, tile_side, tile_side)

    x7, y7 = x0 + third, y0
    x8, y8 = x0, y0 + third
    x1, y1 = x0, y0 + 2*third
    x2, y2 = x0 + third, y0 + 3*third
    x3, y3 = x0 + 2*third, y0 + 3*third
    x4, y4 = x0 + 3*third, y0 + 2*third
    x5, y5 = x0 + 3*third, y0 + third
    x6, y6 = x0 + 2*third, y0
    if line == 2:
        bezier(x7, y7, x7, y7 + third/2, x8 + third/2, y8, x8, y8)
    if line == 3:
        bezier(x7, y7, x7, y7 + third, x1 + third, y1, x1, y1)
    if line == 4:
        bezier(x7, y7, x7, y7 + third/2, x2, y2 - third/2, x2, y2)
    if line == 5:
        bezier(x7, y7, x7, y7 + third*1.5, x3, y3 - third*1.5, x3, y3)
    if line == 6:
        bezier(x7, y7, x7, y7 + third, x4 - third, y4, x4, y4)
    if line == 7:
        bezier(x7, y7, x7, y7 + third, x5 - third, y5, x5, y5)
    if line == 8:
        bezier(x7, y7, x7, y7 + third*0.75, x6, y6 + third*0.75, x6, y6)


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


line = 2


def draw_():
    tile_side = 100
    for line in range(2, 9):
        tile(1.05*tile_side*line, side/2, 100, line)
