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


random.seed(1)


def too_close(x, xs, threshold):
    return any((abs(x-xx) < threshold for xx in xs))


def make_line(point_count, max_x, max_y, distance_threshold):
    x0, y0 = random.randint(0, max_x), 0
    line_points = [(x0, y0)]
    previous_xs = {0, x0, max_x}
    previous_ys = {0, y0, max_y}

    is_vertical = True
    for _ in range(point_count):
        prev_x, prev_y = line_points[-1]
        if is_vertical:
            new_y = prev_y
            while too_close(new_y, previous_ys, threshold=distance_threshold):
                new_y = random.randint(0, max_y)
            line_points.append((prev_x, new_y))
            previous_ys.add(new_y)
        else:
            new_x = prev_x
            while too_close(new_x, previous_xs, threshold=distance_threshold):
                new_x = random.randint(0, max_x)
            line_points.append((new_x, prev_y))
            previous_xs.add(new_x)
        is_vertical = not is_vertical

    penultimate_x, penultimate_y = line_points[-1]
    if is_vertical:
        line_points.append((penultimate_x, max_y))
    else:
        line_points.append((max_x, penultimate_y))

    return line_points


def draw_line(p1, p2, clr, scale=1):
    x1, y1 = p1
    x2, y2 = p2

    stroke(color(255))
    strokeWeight(9)
    strokeCap(PROJECT)
    line(x1*scale, y1*scale, x2*scale, y2*scale)
    stroke(clr)
    strokeWeight(5)
    strokeCap(PROJECT)
    line(x1*scale, y1*scale, x2*scale, y2*scale)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    background(255)
    lines = [make_line(point_count=5,
                       max_x=side,
                       max_y=side,
                       distance_threshold=20)
             for _ in range(5)]
    colors = [color(255, 0, 0), color(0, 255, 0), color(
        0, 0, 255), color(255, 255, 0), color(255, 0, 255)]

    for line_points, line_color in zip(lines, colors):
        for p1, p2 in zip(line_points, line_points[1:]):
            draw_line(p1, p2, line_color)
