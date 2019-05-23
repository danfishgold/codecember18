# Day 23
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_23',
        extension='png'
    )


random.seed(1)
seed = random.randint(1, 10000)

side = 1000


def mid_angle(angle1, angle2):
    mini = min(angle1, angle2)
    maxi = max(angle1, angle2)
    if maxi - mini > PI:
        return mid_angle(mini, maxi - TWO_PI)
    else:
        return (mini + maxi)/2


class RadialLine:
    def __init__(self, p0, angle, dangle, min_drad, max_drad, min_break_distance):
        self.points = [p0]
        self.breaks = []
        self.delta = PVector.fromAngle(angle)
        self.last_break_index = 0
        self.dangle = dangle
        self.min_drad = min_drad
        self.max_drad = max_drad
        self.min_break_distance = min_break_distance

    def add_step(self):
        self.delta = (self.delta
                      .rotate(random.uniform(-1, 1)*self.dangle)
                      .setMag(random.uniform(self.min_drad, self.max_drad)))
        prev_point = self.points[-1]
        new_point = prev_point + self.delta
        self.points.append(new_point)

    def radius(self):
        return self.points[-1].dist(PVector(0.5, 0.5))

    def maybe_split(self, adjacent_line):
        p1 = self.points[-1]
        p2 = adjacent_line.points[-1]
        if p1.dist(p2) > self.min_break_distance:
            f = random.uniform(0.35, 0.65)
            p0 = PVector.lerp(p1, p2, f)
            angle = PVector.lerp(self.delta, adjacent_line.delta, f).heading()
            return RadialLine(p0, angle, self.dangle, self.min_drad, self.max_drad, self.min_break_distance)
        else:
            return None

    def should_add_break(self):
        return self.points[-1].dist(self.points[self.last_break_index]) > self.min_break_distance

    def add_break(self, adjacent_line):
        break_line = (self.points[-1], adjacent_line.points[-1])
        self.last_break_index = len(self.points) - 1
        self.breaks.append(break_line)

    def draw(self, width, height):
        for p1, p2 in zip(self.points, self.points[1:]):
            line(width*p1.x, height*p1.y, width*p2.x, height*p2.y)
        for p1, p2 in self.breaks:
            line(width*p1.x, height*p1.y, width*p2.x, height*p2.y)

    def heading(self):
        return (self.points[-1] - self.points[0]).heading()


lines = []


def setup():
    global lines
    size(side, side)

    center = PVector(0.5, 0.5)
    break_point = (
        center
        + PVector
        .fromAngle(random.uniform(0, TWO_PI))
        .setMag(random.uniform(0, 0.3))
    )

    initial_line_count = 5

    lines = []
    for angle_idx in range(initial_line_count):
        angle = TWO_PI * (angle_idx + random.uniform(0, 0.7)
                          ) / initial_line_count
        line = RadialLine(
            break_point,
            angle,
            dangle=0.002,
            min_drad=0.0015,
            max_drad=0.003,
            min_break_distance=0.025
        )
        lines.append(line)


def mouseClicked():
    redraw()


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


def draw_(seed):
    global lines
    random.seed(seed)
    print 'seed', seed
    background(255)

    for _ in range(30):

        new_lines = []
        for idx, line in enumerate(lines):
            line.add_step()
            if line.should_add_break():
                line.add_break(lines[idx-1])
            maybe_split = line.maybe_split(lines[idx-1])
            if maybe_split:
                new_lines.append(maybe_split)
            new_lines.append(line)

        lines = new_lines

    stroke(0)
    strokeWeight(1)
    for line in lines:
        line.draw(width, height)

    scaffold.hide_outside_circle()
