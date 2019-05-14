# Day 14
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_14',
        extension='png'
    )


side = 500


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    draw_()
    noLoop()


def random_choice(aset):
    return random.choice(list(aset))


HORIZONTAL = 1
VERTICAL = 2


def cool_range(x1, x2):
    return range(min(x1, x2), max(x1, x2)+1)


def cool_2d_range(x1, y1, x2, y2):
    assert x1 == x2 or y1 == y2
    return ((x, y) for x in cool_range(x1, x2) for y in cool_range(y1, y2))


def is_line_ok(x1, y1, x2, y2, orientation, allowed_orientations):
    return all((allowed_orientations.get((x, y), orientation) is orientation
                for x, y in cool_2d_range(x1, y1, x2, y2)
                ))


def other_orientation(orientation):
    if orientation == VERTICAL:
        return HORIZONTAL
    else:
        return VERTICAL


def make_line(point_count, allowed_orientations, n):
    orientation = random.choice((HORIZONTAL, VERTICAL))

    inner_range = list(range(1, n-2))
    if orientation is VERTICAL:
        x0, y0 = random_choice({(x, y)
                                for x in [0, n-1]
                                for y in inner_range
                                if (x, y) not in allowed_orientations})
    else:
        x0, y0 = random_choice({(x, y)
                                for x in inner_range
                                for y in [0, n-1]
                                if (x, y) not in allowed_orientations})
    line_points = [(x0, y0)]
    orientation = other_orientation(orientation)
    for _ in range(point_count):
        prev_x, prev_y = line_points[-1]
        if orientation is VERTICAL:
            new_x = prev_x
            new_y = random_choice(
                filter(lambda y: is_line_ok(prev_x, prev_y, new_x, y, orientation, allowed_orientations), inner_range))
        else:
            new_y = prev_y
            new_x = random_choice(
                filter(lambda x: is_line_ok(prev_x, prev_y, x, new_y, orientation, allowed_orientations), inner_range))

        for x, y in cool_2d_range(prev_x, prev_y, new_x, new_y):
            allowed_orientations[x, y] = other_orientation(orientation)

        line_points.append((new_x, new_y))

        orientation = other_orientation(orientation)

    penultimate_x, penultimate_y = line_points[-1]
    if orientation is VERTICAL:
        last_x = penultimate_x
        last_y = random_choice({
            y
            for y in [0, n-1]
            if is_line_ok(penultimate_x, penultimate_y, last_x, y, orientation, allowed_orientations)
        })
    else:
        last_y = penultimate_y
        last_x = random_choice({
            x
            for x in [0, n-1]
            if is_line_ok(penultimate_x, penultimate_y, x, last_y, orientation, allowed_orientations)
        })
    line_points.append((last_x, last_y))
    for x, y in cool_2d_range(penultimate_x, penultimate_y, last_x, last_y):
        allowed_orientations[x, y] = other_orientation(orientation)

    return line_points


def draw_line(p1, p2, clr, scale=1):
    x1, y1 = p1
    x2, y2 = p2

    xdir = 0 if abs(x1 - x2) < 20/scale else (1 if x2 > x1 else -1)
    ydir = 0 if abs(y1 - y2) < 20/scale else (1 if y2 > y1 else -1)

    if xdir or ydir:
        stroke(color(255))
        strokeWeight(9)
        strokeCap(PROJECT)
        line(x1*scale+xdir*10, y1*scale+ydir*10,
             x2*scale-xdir*10, y2*scale-ydir*10)
    stroke(clr)
    strokeWeight(5)
    strokeCap(ROUND)
    line(x1*scale, y1*scale, x2*scale, y2*scale)


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    n = 40
    line_count = 10

    background(255)

    allowed_orientations = dict()
    lines_and_colors = []
    for idx in range(line_count):
        line = None
        while not line:
            try:
                line = make_line(
                    point_count=5,
                    allowed_orientations=allowed_orientations,
                    n=n)
            except IndexError:
                print 'Failed: board was too full'
        lines_and_colors.append((line, color(255*idx/line_count, 0, 0)))

    random.shuffle(lines_and_colors)
    for line_points, line_color in lines_and_colors:
        for p1, p2 in zip(line_points, line_points[1:]):
            draw_line(p1, p2, line_color, scale=side/(n-1))
