# Day 11: Blokus
from __future__ import division
import scaffold
from collections import defaultdict


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


side = 500
square_count = 50
square_side = side/square_count


class Shape:
    def __init__(self, points):
        self.points = set(points)
        shift_x_plus = {(x+1, y) for (x, y) in points}
        shift_x_minus = {(x-1, y) for (x, y) in points}
        shift_y_plus = {(x, y+1) for (x, y) in points}
        shift_y_minus = {(x, y-1) for (x, y) in points}

        corners = defaultdict(set)
        for pt in self.points.difference(shift_x_plus).difference(shift_y_plus):
            corners[pt].add(0)
        for pt in self.points.difference(shift_x_minus).difference(shift_y_plus):
            corners[pt].add(1)
        for pt in self.points.difference(shift_x_minus).difference(shift_y_minus):
            corners[pt].add(2)
        for pt in self.points.difference(shift_x_plus).difference(shift_y_minus):
            corners[pt].add(3)
        self.corners = dict(corners)

    def __repr__(self):
        return "Shape({}) with corners at {}".format(self.points, self.corners.keys())

    def all_corner_arrangements(self, n0):
        arrangements = []
        for (x0, y0), ns in self.corners.items():
            for n in ns:
                arrangements.append(rotate(self.points, n-n0, (x0, y0)))
        return arrangements


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

shapes = [Shape(pts)
          for pts in [square1, square2,
                      line2, line3, line4, line5,
                      corner22, corner23, corner24, corner33,
                      plus23, plus33]]


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


def draw_():
    draw_board()
    for rowtation in range(4):
        dx, dy = rotation_direction(2-rowtation)
        for index, shape in enumerate(Shape(plus23).all_corner_arrangements(rowtation)):
            x0 = 6 + 6*index
            y0 = 6 + 8*rowtation
            draw_shape(shift(shape, x0, y0), color(0, 255, 0))
            draw_shape({(x0+dx, y0+dy)}, color(255, 0, 0))
