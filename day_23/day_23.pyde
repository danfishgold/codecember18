# Day 23
from __future__ import division
import scaffold
import random


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
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


random.seed(1)
seed = random.randint(1, 10000)

side = 1000


def draw_(seed):
    global triangulation
    random.seed(seed)
    print 'seed', seed
    background(255)
    center = PVector(0.5, 0.5)
    break_point = (
        center
        + PVector
        .fromAngle(random.uniform(0, TWO_PI))
        .setMag(random.uniform(0, 0.1))
    )

    radial_line_count = 50
    radial_line_length = 30

    radial_lines = []
    for angle_idx in range(radial_line_count):
        angle = TWO_PI * (angle_idx+random.uniform(-0.3, 0.3)
                          ) / radial_line_count
        end_point = center + PVector.fromAngle(angle).setMag(0.4)
        delta = 1/radial_line_length * (end_point - break_point)
        radial_line = [break_point]
        for rad_idx in range(radial_line_length):
            delta.rotate(random.uniform(-1, 1)*0.006)
            pt = break_point + (rad_idx+1)*delta
            radial_line.append(pt)
        radial_lines.append(radial_line)

    azimuthal_lines = []
    for az_idx in (range(radial_line_count)):
        idxs1 = sorted(
            random.sample(range(1, radial_line_length), radial_line_length//4)
        )
        idxs2 = sorted(
            random.sample(range(1, radial_line_length), radial_line_length//4)
        )
        for i1, i2 in zip(idxs1, idxs2):
            azimuthal_lines.append(
                (radial_lines[az_idx][i1], radial_lines[az_idx-1][i2])
            )

    stroke(0)
    strokeWeight(1)
    for radial_line in (radial_lines):
        for p1, p2 in zip(radial_line, radial_line[1:]):
            line(width*p1.x, height*p1.y, width*p2.x, height*p2.y)

    for p1, p2 in azimuthal_lines:
        line(width*p1.x, height*p1.y, width*p2.x, height*p2.y)
