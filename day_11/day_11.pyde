# Day 11: Blokus
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


side = 500
square_count = 50
square_side = side/square_count


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
    return rotate({(1, 1)}, -n).pop()


def corners_at_direction(points, n):
    dx, dy = rotation_direction(n)
    shiftx = {(x+dx, y) for (x, y) in points}
    shifty = {(x, y+dy) for (x, y) in points}
    shiftxy = {(x+dx, y+dy) for (x, y) in points}
    return points.difference(shiftx).difference(shifty).difference(shiftxy)


def all_corners(points):
    corners = {0: set(), 1: set(), 2: set(), 3: set()}
    for n in range(4):
        for pt in corners_at_direction(points, n):
            corners[n].add(pt)
    return corners


def all_corner_arrangements(points, n0):
    arrangements = set()
    for n, pts in all_corners(points).items():
        for (x0, y0) in pts:
            arrangements.add(tuple(sorted(rotate(points, n-n0, (x0, y0)))))
    return [set(arr) for arr in arrangements]


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

all_shapes_rotatations = {0: [], 1: [], 2: [], 3: []}
for shape in shapes:
    for n in range(4):
        all_shapes_rotatations[n].extend(all_corner_arrangements(shape, n))


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


n = 0


def mouseClicked():
    global n
    n += 1
    n %= 4
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    draw_board()
    print n
    dx, dy = rotation_direction(n-2)
    for idx, pts in enumerate(all_shapes_rotatations[n]):
        col, row = idx % 7, idx // 7
        for (x, y) in pts:
            draw_shape({(6+6*col+x, 6+6*row+y)}, color(0, 255, 0))
            draw_shape({(6+6*col+dx, 6+6*row+dy)}, color(0, 0, 255))
