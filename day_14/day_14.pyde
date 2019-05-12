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


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    background(255)
    line_points = make_line(
        point_count=20,
        max_x=side,
        max_y=side,
        distance_threshold=20
    )
    line_color = color(255, 0, 0)
    for p1, p2 in zip(line_points, line_points[1:]):
        for weight, clr, cap in [(9, color(255), SQUARE), (5, line_color, PROJECT)]:
            stroke(clr)
            strokeWeight(weight)
            strokeCap(cap)
            noFill()
            line(p1[0], p1[1], p2[0], p2[1])
