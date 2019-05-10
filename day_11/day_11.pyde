# Day 11: Blokus
from __future__ import division
import scaffold
from collections import defaultdict
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


side = 500
square_count = 50
square_side = side/square_count


def all_corners(points):
    corners = defaultdict(set)
    for n in range(4):
        for pt in corners_at_direction(points, n):
            corners[pt].add(n)
    return dict(corners)


def all_corner_arrangements(points, n0):
    arrangements = {}
    for (x0, y0), ns in all_corners(points).items():
        for n in ns:
            arrangements.add(tuple(sorted(rotate(points, n-n0, (x0, y0)))))
    return [set(arr) for arr in arrangements]


def corners_at_direction(points, n):
    dx, dy = rotation_direction(-n)
    shiftx = {(x+dx, y) for (x, y) in points}
    shifty = {(x, y+dy) for (x, y) in points}
    shiftxy = {(x+dx, y+dy) for (x, y) in points}
    return points.difference(shiftx).difference(shifty).difference(shiftxy)


def shift(points, dx, dy):
    return {(dx+x, dy+y) for (x, y) in points}


def rotate(points, n, new_origin=(0, 0)):
    x0, y0 = new_origin
    n = n % 4
    if n == 0:
        def rotator(x, y): return (x, y)
    elif n == 1:
        def rotator(x, y): return (y, -x)
    elif n == 2:
        def rotator(x, y): return (-x, -y)
    elif n == 3:
        def rotator(x, y): return (-y, x)

    return {rotator(x-x0, y-y0) for (x, y) in points}


def rotation_direction(n):
    return rotate({(1, 1)}, n).pop()


def forbidden_points(points):
    return (points
            .union(shift(points, 1, 0))
            .union(shift(points, -1, 0))
            .union(shift(points, 0, 1))
            .union(shift(points, 0, -1)))


square1 = {(0, 0)}
square2 = {(0, 0), (1, 0), (0, 1), (1, 1)}
line2 = {(0, 0), (0, 1)}
line3 = {(0, 0), (0, 1), (0, 2)}
line4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
line5 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
corner22 = {(0, 0), (1, 0), (0, 1)}
corner23 = {(0, 0), (1, 0), (0, 1), (0, 2)}
corner24 = {(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)}
corner33 = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
plus23 = {(0, 0), (0, 1), (0, 2), (1, 1)}
plus33 = {(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}

shapes = [square1, square2,
          line2, line3, line4, line5,
          corner22, corner23, corner24, corner33,
          plus23, plus33]


def draw_shape(shape, color):
    fill(color)
    for (x, y) in shape:
        rect(x*square_side, y*square_side, square_side, square_side)


def draw_board():
    strokeWeight(side // 500 // 2 * 2 + 1)
    stroke(0)
    for rowcol in range(square_count+1):
        line(0, square_side*rowcol, side, square_side*rowcol)
        line(square_side*rowcol, 0, square_side*rowcol, side)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


weird_shape = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)}
square = [(x, y) for x in range(10) for y in range(10)]
weird_shape = set(random.sample(square, len(square) * 3//5))


def draw_():
    draw_board()
    x0, y0 = square_count//2, square_count//2
    shifted_weird_shape = shift(weird_shape, x0, y0)
    forbidden = forbidden_points(shifted_weird_shape)

    draw_shape(shifted_weird_shape, color(0, 255, 0))
    draw_shape(forbidden, color(255, 0, 0, 50))

    for (x, y), directions in all_corners(shifted_weird_shape).items():
        for n in directions:
            dx, dy = rotation_direction(2-n)
            if (x+dx, y+dy) not in forbidden:
                draw_shape({(x+dx, y+dy)}, color(0, 0, 255, 100))
