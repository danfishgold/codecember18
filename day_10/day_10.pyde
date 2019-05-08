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


def point_from_index(x0, y0, tile_side, idx):
    if idx == 0:
        return (x0, y0+tile_side/3)
    if idx == 1:
        return (x0, y0+tile_side*2/3)
    if idx == 2:
        return (x0+tile_side/3, y0+tile_side)
    if idx == 3:
        return (x0+tile_side*2/3, y0+tile_side)
    if idx == 4:
        return (x0+tile_side, y0+tile_side*2/3)
    if idx == 5:
        return (x0+tile_side, y0+tile_side/3)
    if idx == 6:
        return (x0+tile_side*2/3, y0)
    if idx == 7:
        return (x0+tile_side/3, y0)


def normal_at_index(idx, multiplier=1):
    side = idx // 2
    if side == 0:
        return (multiplier, 0)
    elif side == 1:
        return (0, -multiplier)
    elif side == 2:
        return (-multiplier, 0)
    else:
        return (0, multiplier)


def relative_bezier(p1, n1, p2, n2):
    print "n1", n1
    print "n2", n2
    x1, y1 = p1
    x2, y2 = x1 + n1[0], y1 + n1[1]
    x4, y4 = p2
    x3, y3 = x4 + n2[0], y4 + n2[1]
    bezier(x1, y1, x2, y2, x3, y3, x4, y4)


def multipliers(i1, i2):
    if i1 % 2 == 1:
        diff = (i2 - i1) % 8
    else:
        diff = (i1 - i2) % 8

    if diff in [2, 6]:
        return (1/3, 1/3)
    elif diff == 5:
        return (1/2.5, 1/2.5)
    elif diff == 1:
        return (1/6, 1/6)
    elif diff == 3:
        return (0, 0)
    elif diff == 4:
        return (1/2, 1/2)
    elif diff == 7:
        return (1/4.5, 1/4.5)
    else:
        raise ValueError("Bad indexes {} and {}".format(i1, i2))


def path(x0, y0, tile_side, i1, i2):
    p1 = point_from_index(x0, y0, tile_side, i1)
    p2 = point_from_index(x0, y0, tile_side, i2)
    m1, m2 = multipliers(i1, i2)
    n1 = normal_at_index(i1, m1*tile_side)
    n2 = normal_at_index(i2, m2*tile_side)
    strokeWeight(9)
    stroke(255)
    strokeCap(SQUARE)
    relative_bezier(p1, n1, p2, n2)
    strokeWeight(3)
    stroke(0)
    strokeCap(PROJECT)
    relative_bezier(p1, n1, p2, n2)


def tile(xc, yc, tile_side, path_pairs):
    third = tile_side/3
    x0, y0 = xc - tile_side/2, yc - tile_side/2
    stroke(0)
    strokeWeight(2)
    noFill()
    for (i1, i2) in path_pairs:
        path(x0, y0, tile_side, i1, i2)
    # rect(x0, y0, tile_side, tile_side)



side = 1000


def setup():
    size(side, side)
    background(255)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    tile_side = 100
    for i2 in range(7):
        tile(1.05*tile_side*(i2+2), side/2, 100, [(7, i2)])
