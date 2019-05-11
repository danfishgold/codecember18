# Day 13
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_13',
        extension='png'
    )


side = 500
noise_scale = 0.02


def draw_array(array, side):
    min_val = min(array.values())
    max_val = max(array.values())
    for (x, y), val in array.items():
        if is_in_circle(x, y, side):
            stroke(255*ilerp(min_val, max_val, val))
            point(x, y)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def is_in_circle(x, y, side):
    return sqrt((x-side/2)**2 + (y-side/2)**2) < 0.4*side


def find_contours(array, side, thresholds):
    # https://blog.bruce-hill.com/meandering-triangles
    triangles = []
    for x in range(side-1):
        for y in range(side-1):
            triangles.append(((x, y), (x+1, y), (x, y+1)))
            triangles.append(((x+1, y), (x, y+1), (x+1, y+1)))

    contour_segments = dict()
    for threshold in thresholds:
        segments = []
        for triangle in triangles:
            below = [v for v in triangle if array[v] < threshold]
            above = [v for v in triangle if array[v] >= threshold]
            above_minus_below = len(above) - len(below)
            if len(above) == 0 or len(below) == 0:  # meaning above = below = 0
                continue
            elif above_minus_below > 0:
                minority, majority = below, above
            else:
                minority, majority = above, below

            # minority has 1 point. majority has 2
            contour_points = [None, None]
            e1 = minority[0]
            for index, e2 in enumerate(majority):
                how_far = ilerp(array[e1], array[e2], threshold)
                crossing_point = (
                    lerp(e1[0], e2[0], how_far),
                    lerp(e1[1], e2[1], how_far)
                )
                contour_points[index] = crossing_point
            segments.append(tuple(contour_points))
        contour_segments[threshold] = segments
    return contour_segments


def ilerp(a, b, x):
    # Inverse linear interpolation: give the fraction x is away from `a` on a-b
    return (x-a) / (b-a)


def f(x, y):
    r = sqrt((x-side/2) ** 2 + (y-side/2)**2) / (side/2)
    theta = atan2(y, x)
    return 3*sin(TWO_PI*r*2) + 4*sin(theta)


random.seed(1)


def draw_():
    seed = random.randint(1, 1000)
    print 'seed', seed
    noiseSeed(seed)
    array = {(x, y):
             noise(noise_scale*x, noise_scale*y)
             #  if sqrt((x-side/2) ** 2 + (y-side/2)**2) <= 0.4*side
             #  else 1
             for y in range(side)
             for x in range(side)
             }

    # array = {(x, y): f(x, y) for y in range(side) for x in range(side)}
    draw_array(array, side)

    contour_count = 7
    thresholds = [(index+1)/(contour_count+2)
                  for index in range(contour_count)]
    contour_lines = find_contours(array, side, thresholds)
    for segments in contour_lines.values():
        for (p1, p2) in segments:
            if is_in_circle(p1[0], p1[1], side) and is_in_circle(p2[0], p2[1], side):
                stroke(0)
                line(*(p1+p2))