# Day 28
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_28',
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

side = 500


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    line_count = random.randint(5, 100)
    center_count = 2
    print line_count, center_count
    center_radius_fraction = 0.5
    center_phase = 0  # random.uniform(0, TWO_PI)
    # for center_idx in range(center_count):
    #     theta = TWO_PI * center_idx/center_count + center_phase
    #     for x1, y1, x2, y2 in lines_from_center(theta, center_radius_fraction, line_count, 0.4*side):
    #         line(x1, y1, x2, y2)
    intersections = all_intersections(
        0, PI, center_radius_fraction, line_count, 0.4*side)
    polygons = intersection_polygons(intersections, line_count, 0.4*side)
    for pts in polygons.values():
        fill(random.randint(0, 255))
        beginShape()
        for pt in pts:
            vertex(*pt)
        endShape(CLOSE)
    scaffold.hide_outside_circle()


def intersection_polygons(intersections, line_count, max_rad):
    polygons = dict()
    for idx1 in range(line_count):
        for idx2 in range(line_count):
            p1 = intersections.get((idx1, idx2))
            p2 = intersections.get(((idx1+1) % line_count, idx2))
            p3 = intersections.get(((idx1+1) % line_count,
                                    (idx2+1) % line_count))
            p4 = intersections.get((idx1, (idx2+1) % line_count))
            relevant = filter(is_point_ok, (p1, p2, p3, p4))
            polygons[idx1, idx2] = relevant
    return polygons


def is_point_ok(pt):
    if pt is None:
        return False
    # return 0 <= pt[0] <= side and 0 <= pt[1] <= side
    return True


def all_intersections(theta1, theta2, center_radius_fraction, line_count, outer_radius):
    lines1 = lines_from_center(
        theta1, center_radius_fraction, line_count, outer_radius)
    lines2 = lines_from_center(
        theta2, center_radius_fraction, line_count, outer_radius)

    intersections = dict()
    for idx1, (x1, y1, x2, y2) in enumerate(lines1):
        for idx2, (x3, y3, x4, y4) in enumerate(lines2):
            intersections[idx1, idx2] = line_line_intersection(
                x1, y1, x2, y2, x3, y3, x4, y4)
    return intersections


def line_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if denominator == 0:
        return None
    x_nominator = (x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)
    y_nominator = (x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
    return (x_nominator/denominator, y_nominator/denominator)


def lines_from_center(theta, center_radius_fraction, line_count, outer_radius):
    def angle(a): return a - asin(center_radius_fraction*sin(a - theta))
    lines = []
    for line_idx in range(line_count):
        theta1 = angle(PI * line_idx/line_count + theta)
        theta2 = angle(PI * line_idx/line_count + PI + theta)
        x1, y1 = outer_radius*cos(theta1), outer_radius*sin(theta1)
        x2, y2 = outer_radius*cos(theta2), outer_radius*sin(theta2)
        lines.append((side/2 + x1, side/2 + y1, side/2 + x2, side/2 + y2))
    return lines
