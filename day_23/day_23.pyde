# Day 23
from __future__ import division
import scaffold
import random
from delaunay import Triangulation
import poisson_disc


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_23',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed, point_distance=0.07)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 1000


# https://www.color-hex.com/color-palette/78498
colors = [
    color(66, 42, 87),
    color(89, 72, 110),
    color(112, 101, 133),
    color(158, 161, 179),
    color(181, 190, 202),
]


def draw_triangulation(triangulation):
    for (x1, y1), (x2, y2), (x3, y3) in triangulation.triangles():
        clr = random.choice(colors)
        clr = lerpColor(colors[0], colors[-1], random.uniform(0, 1))
        # stroke(255)
        # strokeWeight(1)
        # stroke(clr)
        # fill(clr)
        triangle(width*x1, height*y1, width*x2, height*y2, width*x3, height*y3)


triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))


def draw_(seed, point_distance):
    global triangulation
    random.seed(seed)
    print 'seed', seed
    background(255)
    triangulation = Triangulation(((0, 0), (0, 4), (4, 0)))

    # # Poisson Disc samples
    # theta = acos(1 - point_distance**2 / (2*0.4*0.4))
    # perimiter_count = floor(TWO_PI/theta)

    # perimiter = []
    # for idx in range(perimiter_count):
    #     theta = idx / perimiter_count * TWO_PI
    #     x, y = 0.5 + 0.4*cos(theta), 0.5 + 0.4*sin(theta)
    #     perimiter.append((x, y))

    # for (x, y) in poisson_disc.sample(initial_set=perimiter, r=point_distance):
    #     triangulation.add_point((x, y))

    # Glass
    center = PVector(0.5, 0.5)
    break_point = (
        center
        + PVector
        .fromAngle(random.uniform(0, TWO_PI))
        .setMag(random.uniform(0, 0.1))
    )
    points = [tuple(break_point)[:2]]
    triangulation.add_point(tuple(break_point)[:2])
    for angle_idx in range(100):
        angle = TWO_PI * (angle_idx+random.uniform(-0.3, 0.3)) / 100
        end_point = center + PVector.fromAngle(angle).setMag(0.4)
        for _ in range(30):
            rad = random.uniform(0, 1)**0.75
            pt = PVector.lerp(break_point, end_point, rad)
            points.append(tuple(pt)[:2])
    # for (x, y) in poisson_disc.sample(initial_set=points, r=0.01):
    #     points.append((x, y))
    for pt in points:
        triangulation.add_point(pt)
    # for _ in range(0):
    #     r = random.uniform(0, 0.4)
    #     theta = random.uniform(0, TWO_PI)
    #     x, y = 0.5 + r*cos(theta), 0.5 + r*sin(theta)
    #     triangulation.add_point((x, y))

    draw_triangulation(triangulation)
