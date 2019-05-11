# Day 13
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_13',
        extension='png'
    )


side = 500


def avg(lst):
    return sum(lst)/len(lst)

# https://en.wikipedia.org/wiki/Diamond-square_algorithm


def diamond_square_step(array, n, k):
    if k <= 0:
        return array

    half = 2**(k-1)

    # Diamond step
    middle_range = range(half, 2**n+1, 2*half)
    for x0 in middle_range:
        for y0 in middle_range:
            square_corners = [array[x0+dx*half][y0+dy*half]
                              for (dx, dy) in ((1, 1), (1, -1), (-1, -1), (-1, 1))
                              if 0 <= x0+dx*half < 2**n+1 and 0 <= y0+dy*half < 2**n+1
                              ]
            array[x0][y0] = (avg(square_corners) +
                             random.uniform(-1, 1)*0.5**(n-k))

    # Square step
    middle_range = range(0, 2**n+1, half)
    for x0 in middle_range:
        for y0 in middle_range:
            if (x0/half + y0/half) % 2 == 0:
                continue
            diamond_corners = [array[x0+dx*half][y0+dy*half]
                               for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1))
                               if 0 <= x0+dx*half < 2**n+1 and 0 <= y0+dy*half < 2**n+1
                               ]
            array[x0][y0] = (avg(diamond_corners) +
                             random.uniform(-1, 1)*0.5**(n-k))


n = 9
k = 9
array = [[0 for _ in range(2**n+1)] for _ in range(2**n+1)]


def draw_array(array, n):
    for x in range(2**n+1):
        for y in range(2**n+1):
            stroke(255*array[x][y])
            point(x, y)


def setup():
    size(side, side)
    strokeWeight(ceil(side/500))


def mouseClicked():

    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    diamond_square_step(array, n, k)
    print('min', min((min(row) for row in array)))
    print('max', max((max(row) for row in array)))
    draw_array(array, n)
    global k
    k -= 1
    # ellipse(width/2, height/2, side*0.8, side*0.8)
