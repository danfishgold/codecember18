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


def distance_to_edge(pt):
    return 0.4 - pt.dist(center)


class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r

    @classmethod
    def random_nonintersecting(cls, min_radius, other_circles, max_tries):
        for _ in range(max_tries):
            pt = PVector(
                random.uniform(0.1, 0.9),
                random.uniform(0.1, 0.9)
            )
            circ = cls.add_nonintersecting(pt, other_circles)
            if circ and circ.r > min_radius:
                return circ
        return None

    @classmethod
    def add_nonintersecting(cls, pt, other_circles):
        max_rad = distance_to_edge(pt)
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

    def contains(self, pt):
        self.distance_to_point(pt) <= self.r

    def reached_edge(self):
        return distance_to_edge(self.c) <= self.r

    def draw(self):
        circle(side*self.c.x, side*self.c.y, 2*side*self.r)


circles = []


def setup():
    size(side, side)


min_rad = 0.1


def mouseClicked():
    global circles, min_rad
    # pt = PVector(mouseX/width, mouseY/height)
    # new_circ = Circle.add_nonintersecting(pt, circles)
    new_circ = Circle.random_nonintersecting(min_rad, circles, 1000)
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
    circ = Circle(center, 0.4)
    circ.draw()

    for circ in circles:
        circ.draw()
