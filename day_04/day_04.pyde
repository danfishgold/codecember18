# Day 04: Bouquet
from __future__ import division
import os

base_filename = 'day_04'
extension = 'png'
filename_description = ''

phi = (1 + sqrt(5)) / 2


def keyPressed():
    global filename_description
    if isinstance(key, unicode):
        if key == '\n':
            files = os.listdir('.')
            matches = [
                match(f, r'{}_(\d+).*\.{}'.format(base_filename, extension)) for f in files]
            indexes = [int(m[1]) for m in matches if m is not None]
            if indexes:
                index = max(indexes) + 1
            else:
                index = 1

            if filename_description:
                modifier = '_{}'.format(filename_description.replace(' ', '_'))
            else:
                modifier = ''
            filename = '{}_{:02d}{}.{}'.format(
                base_filename, index, modifier, extension)

            save(filename)
            print 'saved', filename
            filename_description = ''
        else:
            if key == BACKSPACE:
                filename_description = filename_description[:-1]
            else:
                filename_description = filename_description + key


side = 2000

randomSeed(1)


def balloon_petal(theta, length, width):
    pushMatrix()
    rotate(theta)
    wd = 1.6*width
    ht = 1.3*length
    bezier(0, 0, -wd, ht, wd, ht, 0, 0)
    popMatrix()


def ellipse_petal(theta, length, width):
    pushMatrix()
    rotate(theta)
    ellipse(0, length/2, width, length)
    popMatrix()


def exp_decay(f):
    return 1-exp(-4.5*f)


def poly_decay(a, b, pow, f):
    return lerp(a, b, f**pow)


def exp_decay_color(c1, c2, f):
    return lerpColor(c1, c2, exp_decay(f))


def poly_decay_color(c1, c2, pow, f):
    return lerpColor(c1, c2, poly_decay(0, 1, pow, f))


def serp(a, b, f):
    return lerp(a, b, (1 - cos(PI*f))/2)


def serp_color(c1, c2, f):
    return lerpColor(c1, c2, serp(0, 1, f))


def flower_petals(base_length, base_width, count, petal, base_color):
    dtheta = TWO_PI/phi
    inner_stroke = lerpColor(base_color, color(255), 0.6)
    outer_stroke = lerpColor(base_color, color(255), 0.95)
    inner_fill = lerpColor(base_color, color(255), 0)
    outer_fill = lerpColor(base_color, color(255), 0.8)
    draw_commands = []
    for i in range(count)[::-1]:
        f = i/count
        theta = i*dtheta
        fill_color = serp_color(inner_fill, outer_fill,
                                f + randomGaussian()*0.04)
        stroke_color = serp_color(inner_stroke, outer_stroke,
                                  f + randomGaussian()*0.04)
        stroke_weight = serp(2, base_length/20, f)
        length = base_length * serp(0.13, 1, f+randomGaussian()*0.015)
        width = base_width * serp(0.2, 1, f+randomGaussian()*0.03)
        fill(fill_color)
        stroke(stroke_color)
        strokeWeight(stroke_weight)
        draw_commands.append((f, fill_color, stroke_color, stroke_weight,
                              petal, theta, length, width))
        # petal(theta, length, width)
    return draw_commands


def pollen(color, center_radius, count):
    fill(color)
    stroke(255)
    strokeWeight(center_radius/30)
    draw_commands = []
    for _ in range(count):
        r = random(0, center_radius/2)
        theta = random(0, TWO_PI)
        # ellipse(r*cos(theta), r*sin(theta), center_radius/4, center_radius/4)
        draw_commands.append(
            (r*cos(theta), r*sin(theta), center_radius/4))
    return (color, center_radius/30, draw_commands)


def flower(radius, count, petal, petal_color, pollen_color):
    length = radius
    width = 0.4*radius
    center_radius = 0.1*radius
    stroke(0)
    petal_commands = flower_petals(length, width, count, petal, petal_color)
    pollen_commands = pollen(pollen_color, center_radius, 80)
    return (petal_commands, pollen_commands)


def setup():

    size(side, side)
    background(255)

    count = 7
    flower_radius = 0.15*side

    all_petals = []
    all_pollen = []

    for i in range(count):
        resetMatrix()
        if i == count-1:
            cx = width/2
            cy = height/2
        else:
            phase = TWO_PI*i/(count-1)
            # I want to have an outer ring of radius 0.4*side
            radius = 0.4*side - flower_radius
            cx = width/2 + radius*cos(phase)
            cy = height/2 + radius*sin(phase)
        translate(cx, cy)
        colorMode(HSB, 360, 100, 100)
        petal_color = color(317+randomGaussian()*5, 100, 75)
        pollen_color = color(48, 80, 70)
        colorMode(RGB, 255, 255, 255)
        new_petal_commands, new_pollen_commands = flower(radius=flower_radius, count=120,
                                                         petal=balloon_petal, petal_color=petal_color, pollen_color=pollen_color)
        petals_with_translation = [(cx, cy, params)
                                   for params in new_petal_commands]
        all_petals.extend(petals_with_translation)
        all_pollen.append((cx, cy, new_pollen_commands))

    all_petals.sort(key=lambda pet: -pet[2][0])
    for (cx, cy, (f, fill_color, stroke_color, stroke_weight,
                  petal, theta, length, width_)) in all_petals:
        resetMatrix()
        translate(cx, cy)
        fill(fill_color)
        stroke(stroke_color)
        strokeWeight(stroke_weight)
        petal(theta, length, width_)

    for (cx, cy, pollen) in all_pollen:
        print pollen
        (fill_color, stroke_weight, poll) = pollen
        resetMatrix()
        translate(cx, cy)

        fill(fill_color)
        stroke(255)
        strokeWeight(stroke_weight)

        for (x, y, r) in poll:
            ellipse(x, y, r, r)
    noLoop()


def draw():
    pass
