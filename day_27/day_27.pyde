# Day 27
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_27',
        extension='png'
    )


qtr_arcs = [
    (-1, -1, 0, PI/2),
    (+1, -1, PI/2, PI),
    (+1, +1, PI, 3*PI/2),
    (-1, +1, 3*PI/2, 2*PI),
]

half_arcs = [
    (0, -1, 0, PI),
    (+1, 0, PI/2, 3*PI/2),
    (0, +1, PI, 2*PI),
    (-1, 0, 3*PI/2, 5*PI/2),
]


def qtr_circle(x, y, r, direction):
    dx, dy, theta1, theta2 = qtr_arcs[direction]
    arc(x+r/2*dx, y+r/2*dy, 2*r, 2*r, theta1-0.01, theta2+0.01)


def half_circle(x, y, r, direction):
    dx, dy, theta1, theta2 = half_arcs[direction]
    arc(x+r/2*dx, y+r/2*dy, r, r, theta1-0.01, theta2+0.01)


triangle_pts = [
    (+1, +1),
    (-1, +1),
    (-1, -1),
    (+1, -1),
]


def a_triangle(x, y, r, direction):
    pts = [
        (x+r/2, y+r/2),
        (x-r/2, y+r/2),
        (x-r/2, y-r/2),
        (x+r/2, y-r/2),
    ]
    ignored_index = direction
    triangle = triangle_pts[:ignored_index] + triangle_pts[ignored_index+1:]
    beginShape()
    for (dx, dy) in triangle:
        vertex(x+r/2*dx, y+r/2*dy)
    endShape(CLOSE)


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

side = 500

# https://www.color-hex.com/color-palette/72854
colors = [
    color(205, 89, 95),
    color(214, 114, 93),
    color(222, 147, 96),
    color(231, 183, 100),
    # color(240, 221, 103),
]


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)
    side_count = 15
    r = side / (side_count+1)
    xs = scaffold.distribute(0, width, side_count+2)[1:-1]
    ys = scaffold.distribute(0, height, side_count+2)[1:-1]
    noise_scale = 0.02 / (side / 500)
    noiseSeed(seed)
    for x in xs:
        for y in ys:
            shape = random.choice((
                'nothing',
                'circle',
                'square',
                'triangle',
                'qtr circle',
                'half circle',
                # 'circle complement',
                'qtr circle complement',
                'half circle complement'
            ))
            clr = random.choice(colors)
            if shape == 'circle':
                fill(clr)
                stroke(clr)
                circle(x, y, r)
            if shape == 'square':
                fill(clr)
                stroke(clr)
                square(x-r/2, y-r/2, r)
            if shape == 'triangle':
                fill(clr)
                stroke(clr)
                a_triangle(x, y, r, direction=random.randint(0, 3))
            if shape == 'qtr circle':
                fill(clr)
                stroke(clr)
                qtr_circle(x, y, r, direction=random.randint(0, 3))
            if shape == 'circle complement':
                fill(clr)
                noStroke()
                square(x-r/2, y-r/2, r)
                fill(255)
                stroke(255)
                circle(x, y, r)
            if shape == 'qtr circle complement':
                fill(clr)
                noStroke()
                square(x-r/2, y-r/2, r)
                fill(255)
                stroke(255)
                qtr_circle(x, y, r, direction=random.randint(0, 3))
            if shape == 'half circle':
                fill(clr)
                stroke(clr)
                half_circle(x, y, r, direction=random.randint(0, 3))
            if shape == 'half circle complement':
                fill(clr)
                noStroke()
                square(x-r/2, y-r/2, r)
                fill(255)
                stroke(255)
                half_circle(x, y, r, direction=random.randint(0, 3))
