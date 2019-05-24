# Day 26
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_26',
        extension='png'
    )


center = PVector(0.5, 0.5)


class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r

    @classmethod
    def random_nonintersecting(cls, min_radius, other_circles, outer_circle, max_tries):
        for _ in range(max_tries):
            pt = PVector(
                random.uniform(outer_circle.c.x-outer_circle.r,
                               outer_circle.c.x+outer_circle.r),
                random.uniform(outer_circle.c.y-outer_circle.r,
                               outer_circle.c.y+outer_circle.r)
            )
            circ = cls.add_nonintersecting(pt, other_circles, outer_circle)
            if circ and circ.r > min_radius:
                return circ
        return None

    @classmethod
    def add_nonintersecting(cls, pt, other_circles, outer_circle):
        max_rad = outer_circle.r - outer_circle.distance_to_point(pt)
        if max_rad <= 0:
            return None
        for circ in other_circles:
            dist = circ.distance_to_point(pt)
            if dist <= circ.r:
                return None
            else:
                max_rad = min(max_rad, dist - circ.r)
        return cls(pt, max_rad)

    def distance_to_point(self, pt):
        return self.c.dist(pt)

    def draw(self):
        circle(side*self.c.x, side*self.c.y, 2*side*self.r)


def setup():
    size(side, side)


min_rad = 0.1
big_circle = Circle(center, 0.4)
circles = []


def mouseClicked():
    global circles, min_rad
    new_circ = Circle.random_nonintersecting(
        min_rad,
        other_circles=circles,
        outer_circle=big_circle,
        max_tries=2000
    )
    if new_circ:
        circles.append(new_circ)
    else:
        min_rad /= 2

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
    big_circle.draw()

    for circ in circles:
        circ.draw()
