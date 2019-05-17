# Day 18
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_18',
        extension='png'
    )


def setup():
    size(side, side)


def mouseClicked():
    redraw()


random.seed(1)

seed = 1329


def draw():
    global seed
    draw_(seed)
    seed = random.randint(1, 10000)
    noLoop()


def random_choice(aset):
    return random.sample(aset, 1)[0]


white = color(255)


def random_barcode(colors, min_width, max_width, total_width):
    curr_x = 0
    colors = set(colors)
    forbidden_colors = set()
    barcode = []
    while curr_x < total_width:
        # If it's the last one, fill up the space
        if total_width - curr_x < max_width:
            wd = total_width - curr_x
        else:
            wd = random.uniform(min_width, max_width)
            # Make sure there's room for one more
            while total_width - (curr_x+wd) < min_width:
                wd = random.uniform(min_width, max_width)
        clr = random_choice(colors - forbidden_colors)
        barcode.append((curr_x, wd, clr))
        curr_x = curr_x+wd
        forbidden_colors = {clr}
    return barcode


side = 500
# https://visme.co/blog/color-combinations/
# Ornamental reds and yellows
c1 = color(*scaffold.hex_to_rgb('720017', alpha=180))
c2 = color(*scaffold.hex_to_rgb('d9ac2a', alpha=180))


def draw_(seed):
    random.seed(seed)
    print 'seed', seed
    background(255)

    for main_color in [c1, c2]:
        random_rotate()
        barcode = random_barcode([main_color, None], 0.002, 0.01, 1)
        for (x0, wd, clr) in barcode:
            if clr is not None:
                # strokeWeight(1)
                # stroke(clr)
                # noFill()
                noStroke()
                fill(clr)
                # rect(floor(x0*side), 0, floor(wd*side), height)
                project(x0, wd, side, side*3, center=width/2)
    hide_outside_circle()


def project(x, wd, f1, f2, center):
    x0 = x-0.5
    beginShape()
    vertex(center + floor(x0*f1), 0)
    vertex(center + floor(x0*f2), height)
    vertex(center + floor((x0+wd)*f2), height)
    vertex(center + floor((x0+wd)*f1), 0)
    endShape(CLOSE)


def hide_outside_circle():
    strokeWeight(side)
    stroke(color(255))
    noFill()
    ellipse(width/2, height/2, 1.8*side, 1.8*side)


def random_rotate():
    translate(width/2, height/2)
    rotate(random.uniform(0, TWO_PI))
    translate(-width/2, -height/2)
