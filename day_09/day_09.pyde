# Day 09: Triangles
from __future__ import division
import os
import random

base_filename = 'day_09'
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


def p1(x, y):
    # See my notes
    if x % 2 == 0:
        return (side/2 - triangle_side/2 + x/2 * triangle_side + y * triangle_side/2,
                side/2 - sqrt(3)/6*triangle_side + y * sqrt(3)/2*triangle_side)
    else:
        return p1(x-1, y+1)


def triangle_points(x, y):
    # See my notes
    x1, y1 = p1(x, y)
    x2, y2 = x1 + triangle_side, y1
    x3 = x1 + triangle_side/2
    if x % 2 == 0:
        y3 = y1 + sqrt(3)/2 * triangle_side
    else:
        y3 = y1 - sqrt(3)/2 * triangle_side
    return (x1, y1), (x2, y2), (x3, y3)


def tri(x, y):
    (x1, y1), (x2, y2), (x3, y3) = triangle_points(x, y)
    triangle(x1, y1, x2, y2, x3, y3)


def is_point_in_center(x, y):
    return sqrt((x-side/2)**2 + (y-side/2)**2) <= 0.4*side


def is_triangle_in_center(x, y):
    p1, p2, p3 = triangle_points(x, y)
    return is_point_in_center(*p1) and is_point_in_center(*p2) and is_point_in_center(*p3)


def neighbors(x, y):
    if x % 2 == 0:
        potentials = [(x-1, y), (x+1, y), (x+1, y-1)]
    else:
        potentials = [(x-1, y), (x+1, y), (x-1, y+1)]

    return {pt for pt in potentials if is_triangle_in_center(*pt)}


green = color(101, 155, 94)
side = 500
triangle_side = side // 500 * 19

x_radius = side // triangle_side + 5
y_radius = int((side/2) / (triangle_side * sqrt(3)/2)) + 5
all_triangles = {(x, y)
                 for y in range(-y_radius, y_radius)
                 for x in range(-x_radius-y, x_radius-y)
                 if is_triangle_in_center(x, y)}


def setup():
    size(side, side)
    background(255)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


random.seed(1)


def draw_():
    seed = random.randint(0, 10000)
    print "seed:", seed
    random.seed(seed)

    noStroke()
    fill(0)

    for (x, y) in all_triangles:
        if x % 2 == 0:
            fill(0)
        else:
            fill(120)
        tri(x, y)
    fill(255)
    tri(0, 0)
