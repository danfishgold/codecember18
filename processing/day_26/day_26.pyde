# Day 26: Packing
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

    def pack(self, max_radius_fraction, min_radius_fraction):
        inner_circles = []
        radius_fraction = max_radius_fraction
        while radius_fraction > min_radius_fraction:
            rad = radius_fraction*self.r
            new_circle = Circle.random_nonintersecting(
                rad,
                other_circles=inner_circles,
                outer_circle=self,
                max_tries=2000
            )
            if new_circle:
                inner_circles.append(new_circle)
            else:
                radius_fraction /= 2
        return inner_circles


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
seed = 4549  # random.randint(1, 10000)

side = 2000


# https://www.color-hex.com/color-palette/78496
colors = [
    color(255, 191, 144),
    color(221, 68, 51),
    color(0, 153, 153),
    color(207, 121, 46),
    color(103, 0, 51),
]


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    big_circle = Circle(center, 0.4)

    pack = big_circle.pack(0.1, 0.01)

    for circ in pack:
        fill(random.choice(colors))
        noStroke()
        circ.draw()
