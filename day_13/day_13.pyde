# Day 13
from __future__ import division
import scaffold
import random
import collections


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_13',
        extension='png'
    )


side = 500
noise_scale = 0.02


def draw_array(array, scale):
    for (x, y), val in array.items():
        stroke(255*val)
        point(scale*x, scale*y)


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


Triangle = collections.namedtuple("Triangle", "v1 v2 v3")
Edge = collections.namedtuple("Edge", "e1 e2")


def draw_():
    noiseSeed(random.randint(1, 1000))
    array = {(x, y): noise(noise_scale*x, noise_scale*y)
             for y in range(side)
             for x in range(side)
             if sqrt((x-side/2)**2 + (y-side/2)**2) else 0}

    # https://blog.bruce-hill.com/meandering-triangles
    triangles = []
    for x in range(0, side-1):
        for y in range(0, side-1):
            t1 = Triangle((x, y), (x+1, y), (x, y+1))
            triangles.append(t1)
            t2 = Triangle((x+1, y), (x, y+1), (x+1, y+1))
            triangles.append(t2)

    contour_segments = []
    for threshold in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        for triangle in triangles:
            below = [v for v in triangle if array[v] < threshold]
            above = [v for v in triangle if array[v] >= threshold]
            if len(below) == 0 or len(above) == 0:
                continue
            minority = above if len(above) < len(below) else below
            majority = above if len(above) > len(below) else below

            contour_points = []
            crossed_edges = (Edge(minority[0], majority[0]),
                             Edge(minority[0], majority[1]))
            for triangle_edge in crossed_edges:
                # how_far is a number between 0 and 1 indicating what percent
                # of the way along the edge (e1,e2) the crossing point is
                e1, e2 = triangle_edge.e1, triangle_edge.e2
                how_far = ((threshold - array[e2])
                           / (array[e1] - array[e2]))
                crossing_point = (
                    lerp(e1[0], e2[0], how_far),
                    lerp(e1[1], e2[1], how_far)
                )
                contour_points.append(crossing_point)
            contour_segments.append(Edge(contour_points[0], contour_points[1]))

    draw_array(array, 1)
    for (p1, p2) in contour_segments:
        stroke(0)
        line(*(p1+p2))
