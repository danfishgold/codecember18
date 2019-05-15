# Day 16
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_16',
        extension='png'
    )


side = 1000


def ring(r1, r2, clr=color(0)):
    if not clr:
        return
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    diam = r1+r2
    ellipse(width/2, height/2, diam, diam)


def marc(r1, r2, theta1, theta2, clr=color(0)):
    if not clr:
        return
    stroke(clr)
    strokeWeight(abs(r2-r1) + 1)
    strokeCap(SQUARE)
    diam = r1+r2
    arc(width/2, height/2, diam, diam, theta1-0.005, theta2+0.005)


def dr(r, pixels):
    return r*TWO_PI/pixels


def rs(r, pixels, r_count=10):
    radiuses = [r]
    for _ in range(r_count-1):
        prev = radiuses[-1]
        radiuses.append(prev-dr(prev, pixels))
    return radiuses


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    draw_()
    noLoop()


def random_color():
    # return color(
    #     random.randint(0, 255),
    # )
    return color(0)


def generate_pattern(rows, cols):
    return [[
        random_color() if random.randint(0, 1) else None
        for _ in range(cols)]
        for _ in range(rows)]


def generate_restrictive_pattern(rows, cols):
    first_row = [random_color() if random.randint(0, 1) else None
                 for _ in range(cols)]
    pattern = [first_row]
    for row in range(1, rows):
        prev = pattern[-1]
        is_ok = False
        while not is_ok:
            new = [random_color() if random.randint(0, 1) else None
                   for _ in range(cols)]
            is_ok = True
            for col in range(cols):
                bad1 = (prev[col-1] and not prev[col]
                        and not new[col-1] and new[col])

                bad2 = (not prev[col-1] and prev[col]
                        and new[col-1] and not new[col])

                bad3 = (prev[(col+1) % cols] and not prev[col]
                        and not new[(col+1) % cols] and new[col])

                bad4 = (not prev[(col+1) % cols] and prev[col]
                        and new[(col+1) % cols] and not new[col])

                is_ok = is_ok and (not (bad1 or bad2 or bad3 or bad4))
        pattern.append(new)
    return pattern


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    random.seed(seed)
    print 'seed', seed
    copies = random.randint(5, 15)
    pixels_per_copy = random.randint(3, 7)
    rows = 15
    pixel_count = pixels_per_copy*copies
    pattern = generate_restrictive_pattern(rows, pixels_per_copy)
    dtheta = TWO_PI/pixel_count
    background(255)
    noFill()

    rads = rs(side*0.4, pixels=pixel_count, r_count=rows+1)
    for copy_index in range(copies):
        for row in range(rows):
            for col in range(pixels_per_copy):
                marc(
                    rads[row],
                    rads[row+1],
                    (copy_index*pixels_per_copy + col)*dtheta,
                    (copy_index*pixels_per_copy + col+1) * dtheta,
                    pattern[row][col]
                )

    # for row in range(rows):
    #     for col in range(pixels_per_copy):
    #         if pattern[row][col]:
    #             noStroke()
    #             fill(pattern[row][col])
    #             square(col*20, row*20, 20)
