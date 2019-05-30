# Day 29: Polygon Lines
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
seed = 7667  # random.randint(1, 10000)

side = 2000

# https://www.color-hex.com/color-palette/78728
colors = [
    color(61, 61, 93),
    color(255, 191, 67),
    color(238, 25, 45),
]


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
                                  n=4, theta0=random.uniform(0, TWO_PI)),
        regular_polygon_in_circle(side/2, side/2, side*0.4,
                                  n=3, theta0=random.uniform(0, TWO_PI)),
        regular_polygon_in_circle(side/2, side/2, side*0.3,
                                  n=4, theta0=random.uniform(0, TWO_PI)),
    ]
    base_angle = random.uniform(0, TWO_PI)
    angles = [base_angle + angle +
              random.uniform(-1, 1)*0.1*PI for angle in (0, 1/3*TWO_PI, 2/3*TWO_PI)]
    for polygon, angle, clr in zip(polygons, angles, colors):
        lines = polygon_lines(polygon, angle, line_width)
        all_lines.append([(ln, clr) for ln in lines])

    for ln, clr in interlace(all_lines):
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
    line_count = floor(diameter / line_width)+1
    pad = (diameter - line_count*line_width)/2
    npad = pad / abs(cos(angle))
    intersection_lines = []
    for line_idx in range(line_count):
        intersections = []
        n = nmin + npad + line_idx*line_width/abs(cos(angle))
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


def random_circle(min_rad):
    max_rad = min_rad
    while not max_rad > min_rad:
        r = random.uniform(0, side*0.4)
        theta = random.uniform(0, TWO_PI)
        x, y = side/2+r*cos(theta), side/2+r*sin(theta)
        max_rad = side*0.4 - r
    rad = random.uniform(min_rad, max_rad)
    return (x, y, rad)


def interlace(lists):
    max_len = max(len(lst) for lst in lists)
    for idx in range(max_len):
        for lst in lists:
            if idx < len(lst):
                yield lst[idx]
