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


def make_line(point_count, forbidden_points, n):
    is_vertical = random.randint(0, 1) == 1
    inner_range = list(range(1, n-2))
    if is_vertical:
        x0, y0 = random_choice({(x, y)
                                for x in [0, n-1]
                                for y in inner_range
                                if (x, y) not in forbidden_points})
    else:
        x0, y0 = random_choice({(x, y)
                                for x in inner_range
                                for y in [0, n-1]
                                if (x, y) not in forbidden_points})
    line_points = [(x0, y0)]
    is_vertical = not is_vertical
    for _ in range(point_count):
        prev_x, prev_y = line_points[-1]
        if is_vertical:
            new_x = prev_x
            new_y = random_choice(
                filter(lambda y: (new_x, y) not in forbidden_points, inner_range))
        else:
            new_y = prev_y
            new_x = random_choice(
                filter(lambda x: (x, new_y) not in forbidden_points, inner_range))

        for x in range(min(prev_x, new_x), max(prev_x, new_x)+1):
            for y in range(min(prev_y, new_y), max(prev_y, new_y)+1):
                forbidden_points.add((x, y))

        line_points.append((new_x, new_y))

        is_vertical = not is_vertical

    penultimate_x, penultimate_y = line_points[-1]
    if is_vertical:
        last_x = penultimate_x
        last_y = random_choice({
            y
            for y in [0, n-1]
            if (last_x, y) not in forbidden_points
        })
    else:
        last_y = penultimate_y
        last_x = random_choice({
            x
            for x in [0, n-1]
            if (x, last_y) not in forbidden_points
        })
    line_points.append((last_x, last_y))
    for x in range(min(penultimate_x, last_x), max(penultimate_x, last_x)+1):
        for y in range(min(penultimate_y, last_y), max(penultimate_y, last_y)+1):
            forbidden_points.add((x, y))

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


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed

    n = 40

    background(255)

    forbidden_points = set()
    lines_and_colors = []
    for idx in range(10):
        line = None
        while not line:
            try:
                line = make_line(
                    point_count=5,
                    forbidden_points=forbidden_points,
                    n=n)
            except IndexError:
                print 'Failed: board was too full'
        lines_and_colors.append((line, color(255*idx/10, 0, 0)))

    for line_points, line_color in lines_and_colors:
        for p1, p2 in zip(line_points, line_points[1:]):
            draw_line(p1, p2, line_color, scale=side/(n-1))
