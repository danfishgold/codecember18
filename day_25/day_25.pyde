# Day 25
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_25',
        extension='png'
    )


def projected_point(pt, transformation):
    a, b, c = transformation[0]
    d, e, f = transformation[1]
    g, h, i = transformation[2]
    x = a*pt.x + b*pt.y + c*pt.z
    y = d*pt.x + e*pt.y + f*pt.z
    z = g*pt.x + h*pt.y + i*pt.z
    return PVector(x/z, y/z, 1)


class Box:
    def __init__(self, x0, y0, z0, wd, ht, dp):
        self.p0 = PVector(x0, y0, z0)
        self.x = PVector(wd, 0, 0)
        self.y = PVector(0, ht, 0)
        self.z = PVector(0, 0, dp)

    def projected_lines(self, transformation):
        lines = []
        for p1, p2 in self.lines():
            lines.append((
                projected_point(p1, transformation),
                projected_point(p2, transformation)
            ))
        return lines

    def lines(self):
        dirs = (self.x, self.y, self.z)
        lines = []
        for idx in range(3):
            active = dirs[idx % 3]
            static1 = dirs[(idx+1) % 3]
            static2 = dirs[(idx+2) % 3]
            for s1 in (0, 1):
                for s2 in (0, 1):
                    p1 = self.p0 + s1*static1 + s2*static2
                    p2 = p1 + active
                    lines.append((p1, p2))
        return lines

    def draw(self, x0, y0, transformation):
        for p1, p2 in self.projected_lines(transformation):
            line(x0+width*p1.x, y0+height*p1.y, x0+width*p2.x, y0+height*p2.y)


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

    boxes = []
    box_distance = 0.1
    box_side = box_distance*0.5
    box_side_count = 10
    offset = 0.5 * (1 - box_side_count*box_distance +
                    box_distance - box_side)
    for x in range(box_side_count):
        for y in range(box_side_count):
            box = Box(
                x0=box_distance*x,
                y0=box_distance*y,
                z0=1,
                wd=box_side,
                ht=box_side,
                dp=box_side*0.5
            )
            boxes.append(box)

    transformation = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    for box in boxes:
        box.draw(offset*width, offset*height, transformation)
