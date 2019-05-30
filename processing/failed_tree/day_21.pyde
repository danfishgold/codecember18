# Day 21
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_21',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


up = PVector(0, -1)
degrees = TWO_PI/360


def angle_to_up(v):
    angle = atan2(v.y, v.x) + PI/2
    return ((angle+PI) % TWO_PI) - PI


class Branch:
    def __init__(self, initial_position, direction):
        self.position = initial_position
        self.direction = direction
        self.history = [tuple(self.position)[:2]]
        self.last_split = None

    def advance(self, dx, up_factor, random_factor):
        angle = angle_to_up(self.direction)
        if abs(angle) < up_factor:
            move_on_up = angle
        elif angle > 0:
            move_on_up = -up_factor
        else:
            move_on_up = +up_factor
        self.direction.rotate(move_on_up + random.uniform(-1, 1)*random_factor)
        self.position = self.position + self.direction*dx
        self.history.append(tuple(self.position)[:2])

    def split(self):
        # rotation = random.choice((1, -1)) * random.uniform(PI/4, PI/3)
        rotation = random.choice((1, -1)) * PI/3
        new_direction = self.direction.copy().rotate(rotation)
        self.last_split = len(self.history)
        return Branch(self.position.copy(), new_direction)

    def should_split(self):
        length = len(self.history)
        if self.last_split:
            last_branch_out = length - self.last_split
        else:
            last_branch_out = length

        # prob = min(1, max(0, last_branch_out - 10)/100) ** 4
        # return random.random() < prob
        # if abs(angle_to_up(self.direction)) < 20*degrees:
        return random.random() < 0.01


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 500


def draw_(seed=None):
    random.seed(seed)
    print 'seed', seed
    background(255)
    n = 1
    root = Branch(
        PVector(width/2, height),
        up.copy()
    )

    for _ in range(50):
        root.advance(1, up_factor=0.5*degrees, random_factor=1*degrees)
    branches = [root]
    for _ in range(250):
        for branch in branches:
            branch.advance(1, up_factor=0.2*degrees, random_factor=3*degrees)
            if branch.should_split():
                branches.append(branch.split())

    for branch in branches:
        length = len(branch.history)
        for idx, (pt1, pt2) in enumerate(zip(branch.history, branch.history[1:])):
            f = 1 - idx/length
            strokeWeight(f**0.5 * length/10)
            stroke(lerpColor(color(200, 255, 200), color(0, 100, 0), f))
            line(*(pt1+pt2))
