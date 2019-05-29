# Day 29
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_29',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 1000


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    line_width = 10 * side // 500
    all_lines = []
    polygons = [random_polygon_in_circle(
        side/2, side/2, side*0.4, n=3) for _ in range(3)]
    polygons = [
        regular_polygon_in_circle(side/2, side/2, side*0.4,
                                  n=3, theta0=random.uniform(0, TWO_PI)),
        regular_polygon_in_circle(side/2, side/2, side*0.4,
                                  n=4, theta0=random.uniform(0, TWO_PI)),
        regular_polygon_in_circle(side/2, side/2, side*0.4,
                                  n=5, theta0=random.uniform(0, TWO_PI)),
    ]
    for polygon in polygons:
        lines = polygon_lines(polygon, random.uniform(0, TWO_PI), line_width)
        clr = random_color()
        all_lines.extend((ln, clr) for ln in lines)

    random.shuffle(all_lines)
    for ln, clr in all_lines:
        stroke(clr)
        strokeWeight(line_width/2)
        if len(ln) == 2:
            (x1, y1), (x2, y2) = ln
            line(x1, y1, x2, y2)
        elif len(ln) == 1:
            point(*ln[0])
        else:
            raise IndexError("Weird number of points on line")


def polygon_lines(pts, angle, line_width):
    m = tan(angle)
    ns = [y - m*x for (x, y) in pts]
    nmin = min(ns)
    nmax = max(ns)
    dn = nmax - nmin
    diameter = dn * abs(cos(angle))
    line_count = (floor(diameter / line_width) + 1) // 2 * 2
    n0 = nmin  # - (line_count*line_width - diameter) / 2

    intersection_lines = []
    for line_idx in range(line_count):
        intersections = []
        n = n0 + dn * line_idx / line_count
        stroke(100)
        # line(-50, -50*m+n+5, 700, 700*m+n+5)
        for line_idx in range(len(pts)):
            x1, y1 = pts[line_idx-1]
            x2, y2 = pts[line_idx]

            x = (y1*x2-y2*x1 - n*(x2-x1)) / (y1-y2 + m*(x2-x1))
            if min(x1, x2) <= x <= max(x1, x2):
                y = m*x+n
                if x1 == x2 and not min(y1, y2) <= y <= max(y1, y2):
                    continue
                intersections.append((x, y))
        if len(intersections) in (1, 2):
            intersection_lines.append(intersections)
        elif len(intersections) != 0:
            print 'weird intersections:', intersections
            for pt in intersections:
                circle(pt[0], pt[1], 10)
    return intersection_lines


def random_point():
    return (random.uniform(0.1*side, 0.9*side),
            random.uniform(0.1*side, 0.9*side))


def random_polygon_in_circle(x, y, r, n=None):
    thetas = sorted(random.uniform(0, TWO_PI)
                    for _ in range(n or random.randint(3, 6)))
    while min((t2-t1) % TWO_PI for (t1, t2) in zip(thetas, thetas[1:]+thetas[0:1])) < PI*0.2:
        thetas = sorted(random.uniform(0, TWO_PI)
                        for _ in range(n or random.randint(3, 6)))
    return polygon_in_circle(x, y, r, thetas)


def regular_polygon_in_circle(x, y, r, n=None, theta0=0):
    n = n or 3
    thetas = (theta0 + TWO_PI*idx/n for idx in range(n))
    return polygon_in_circle(x, y, r, thetas)


def polygon_in_circle(x, y, r, thetas):
    return tuple((x+r*cos(theta), y+r*sin(theta)) for theta in thetas)


def draw_polygon(polygon):
    beginShape()
    for pt in polygon:
        vertex(*pt)
    endShape(CLOSE)


def random_color():
    return color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
