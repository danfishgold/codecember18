# Day 14: Pipes
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_14',
        extension='png'
    )


side = 2000


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
    return [(x, y) for x in cool_range(x1, x2) for y in cool_range(y1, y2)]


def is_line_ok(x1, y1, x2, y2, orientation, allowed_orientations):
    return (
        all((allowed_orientations.get((x, y), orientation) is orientation
             for x, y in cool_2d_range(x1, y1, x2, y2)[1:-1]
             ))
        and (x2, y2) not in allowed_orientations
    )


def other_orientation(orientation):
    if orientation == VERTICAL:
        return HORIZONTAL
    else:
        return VERTICAL


def pick_next_point(prev_x, prev_y, orientation, allowed_orientations, options):
    if orientation is VERTICAL:
        new_x = prev_x
        new_y = random_choice(
            filter(lambda y: is_line_ok(prev_x, prev_y, new_x, y, orientation, allowed_orientations) and y != prev_y, options))
    else:
        new_y = prev_y
        new_x = random_choice(
            filter(lambda x: is_line_ok(prev_x, prev_y, x, new_y, orientation, allowed_orientations) and x != prev_x, options))

    return (new_x, new_y)


def make_line(point_count, allowed_orientations, n):
    orientation = random.choice((HORIZONTAL, VERTICAL))

    inner_range = list(range(1, n-2))
    outer_range = [0, n-1]
    if orientation is HORIZONTAL:
        x0, y0 = random_choice({(x, y)
                                for x in outer_range
                                for y in inner_range
                                if (x, y) not in allowed_orientations})
    else:
        x0, y0 = random_choice({(x, y)
                                for x in inner_range
                                for y in outer_range
                                if (x, y) not in allowed_orientations})
    line_points = [(x0, y0)]
    for idx in range(point_count+1):
        prev_x, prev_y = line_points[-1]
        new_x, new_y = pick_next_point(
            prev_x, prev_y,
            orientation, allowed_orientations,
            options=outer_range if idx == point_count else inner_range
        )
        next_orientation = other_orientation(orientation)
        for x, y in cool_2d_range(prev_x, prev_y, new_x, new_y):
            allowed_orientations[x, y] = next_orientation

        line_points.append((new_x, new_y))

        orientation = next_orientation

    return line_points


def draw_pipe(pipe, clr, xs, ys):
    mult = side//500//2*2+1
    draw_line(pipe[0], pipe[1], xs, ys, color(255), mult*9)
    for (p1, p2, p3) in zip(pipe, pipe[1:], pipe[2:]):
        draw_line(p2, p3, xs, ys, color(255), mult*9)
        draw_line(p1, p2, xs, ys, clr, mult*5)
        draw_line(p2, p3, xs, ys, clr, mult*5)


def draw_line(p1, p2, xs, ys, clr, stroke_weight):
    x1, y1 = xs[p1[0]], ys[p1[1]]
    x2, y2 = xs[p2[0]], ys[p2[1]]

    stroke(clr)
    strokeWeight(stroke_weight)
    strokeCap(ROUND)
    line(x1, y1, x2, y2)


random.seed(2)


def random_xs(n, side, min_dist):

    xs = [min_dist * idx for idx in range(n)]
    while xs[-1] < side:
        idx0 = random.randint(1, n-1)
        for idx in range(idx0, n):
            xs[idx] += 1
    return xs


def draw_():
    seed = 9285  # random.randint(1, 10000)
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

    xs = random_xs(n, side, 5)
    ys = random_xs(n, side, 5)

    for line_points, line_color in lines_and_colors:
        draw_pipe(line_points, line_color, xs, ys)
