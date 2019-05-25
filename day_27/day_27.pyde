# Day 27
from __future__ import division
import scaffold
import random
from collections import defaultdict


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


def random_shape_with_connections(connections):
    connections = set(connections)
    if len(connections) == 4:
        # shape = random.choice(('square', 'circle complement'))
        shape = 'square'
        params = []
    if len(connections) == 0:
        # shape = random.choice(('nothing', 'circle'))
        shape = 'nothing'
        params = []
    if len(connections) == 3:
        direction = set(range(4)).difference(connections).pop()
        # shape = 'half circle complement'
        shape = 'square'
        params = [direction]
    if len(connections) == 1:
        direction = connections.pop()
        shape = 'half circle'
        params = [direction]
    if len(connections) == 2:
        dir1, dir2 = tuple(connections)
        if abs(dir1-dir2) == 2:
            # there are no shapes with only opposite connections
            return random_shape_with_connections(range(4))
        if abs(dir1-dir2) == 3:
            direction = max(dir1, dir2)
        else:
            direction = min(dir1, dir2)
        shape = random.choice(
            ('qtr circle', 'qtr circle complement', 'triangle'))
        params = [(direction+1) % 4]

    return shape, params


def draw_shape(x, y, r, shape, params, clr):
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
        a_triangle(x, y, r, direction=params[0])
    if shape == 'qtr circle':
        fill(clr)
        stroke(clr)
        qtr_circle(x, y, r, direction=params[0])
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
        a_triangle(x, y, r, params[0])
        fill(255)
        stroke(255)
        qtr_circle(x, y, r, direction=(params[0]+2) % 4)
    if shape == 'half circle':
        fill(clr)
        stroke(clr)
        half_circle(x, y, r, direction=params[0])
    if shape == 'half circle complement':
        fill(clr)
        noStroke()
        square(x-r/2, y-r/2, r)
        fill(255)
        stroke(255)
        half_circle(x, y, r, direction=params[0])


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
    side_count = 25
    noise_scale = 5 / side_count
    noiseSeed(seed)

    r = side / (side_count+1)
    xs = scaffold.distribute(0, width, side_count+2)[1:-1]
    ys = scaffold.distribute(0, height, side_count+2)[1:-1]

    filled = defaultdict(bool)
    for x_idx in range(side_count):
        for y_idx in range(side_count):
            val = noise(noise_scale*x_idx, noise_scale*y_idx)
            filled[x_idx, y_idx] = val > 0.45

    for x_idx, x in enumerate(xs):
        for y_idx, y in enumerate(ys):
            # if filled[x_idx, y_idx]:
            #     noStroke()
            #     fill(0, 0, 0, 40)
            #     square(x-r/2, y-r/2, r)

            if filled[x_idx, y_idx]:
                connections = []
                if filled[x_idx, y_idx-1]:
                    connections.append(0)
                if filled[x_idx+1, y_idx]:
                    connections.append(1)
                if filled[x_idx, y_idx+1]:
                    connections.append(2)
                if filled[x_idx-1, y_idx]:
                    connections.append(3)
            else:
                connections = []
            print connections
            shape, params = random_shape_with_connections(connections)
            draw_shape(x, y, r, shape, params, random.choice(colors))
