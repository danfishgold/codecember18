# Day 19
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_19',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def generate_lines(line_length, line_count, shift):

    first_line = [0 for _ in range(line_length)]
    lines = [first_line]
    for _ in range(line_count-1):
        new_line = generate_line(lines[-1], shift)
        lines.append(new_line)

    return lines


def generate_line(prev_line, shift):
    padded = [prev_line[0]] + prev_line + [prev_line[-1]]
    triplets = zip(padded, padded[1:], padded[2:])
    if shift > 0:
        line = map(max, triplets)
    else:
        line = map(min, triplets)

    range_length = random.randint(4, 5)
    start = random.randint(0, len(prev_line)-range_length)
    end = start+range_length
    for idx in range(start, end):
        line[idx] += shift
    return line


def draw_line(line, x0, height):
    beginShape()
    dy = height/len(line)
    for idx, x in enumerate(line):
        vertex(x0+x, dy*idx)
        vertex(x0+x, dy*(idx+1))
    endShape()


random.seed(1)


def draw():
    seed = random.randint(1, 10000)
    draw_(
        line_length=50,
        line_count=50,
        seed=seed)
    noLoop()


side = 500


def draw_(line_length, line_count, seed=None):
    random.seed(seed)
    print 'seed', seed
    background(255)

    stroke(0)
    strokeWeight(3)
    noFill()

    positive_lines = generate_lines(
        line_length,
        line_count//2,
        shift=height/line_length,
    )
    negative_lines = generate_lines(
        line_length,
        line_count//2,
        shift=-height/line_length,
    )

    lines = negative_lines[:0:-1] + positive_lines
    dx = width / line_count
    for idx, line in enumerate(lines):
        x = (idx+1)*dx
        draw_line(line, x, height)


    scaffold.hide_outside_circle()
