# Day 04
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


side = 1000

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
    for i in range(count)[::-1]:
        f = i/count
        theta = i*dtheta
        fill_color = serp_color(inner_fill, outer_fill,
                                f + randomGaussian()*0.04)
        stroke_color = serp_color(inner_stroke, outer_stroke,
                                  f + randomGaussian()*0.04)
        length = base_length * serp(0.13, 1, f+randomGaussian()*0.015)
        width = base_width * serp(0.2, 1, f+randomGaussian()*0.03)
        fill(fill_color)
        stroke(stroke_color)
        strokeWeight(serp(2, base_length/20, f))
        petal(theta, length, width)


def pollen(color, center_radius, count):
    fill(color)
    stroke(255)
    strokeWeight(center_radius/30)
    for _ in range(count):
        r = random(0, center_radius/2)
        theta = random(0, TWO_PI)
        ellipse(r*cos(theta), r*sin(theta), center_radius/4, center_radius/4)


def flower(radius, count, petal, petal_color, pollen_color):
    length = radius
    width = 0.4*radius
    center_radius = 0.1*radius
    stroke(0)
    flower_petals(length, width, count, petal, petal_color)
    pollen(pollen_color, center_radius, 80)


def setup():

    size(side, side)
    background(255)

    count = 8
    flower_radius = 0.16*side

    for i in range(count):
        resetMatrix()
        if i == count-1:
            translate(width/2, height/2)
        else:
            phase = TWO_PI*i/(count-1)
            # I want to have an outer ring of radius 0.4*side
            radius = 0.4*side - flower_radius
            translate(width/2 + radius*cos(phase),
                      height/2 + radius*sin(phase))
        colorMode(HSB, 360, 100, 100)
        petal_color = color(317+randomGaussian()*5, 100, 65)
        pollen_color = color(48, 100, 82)
        colorMode(RGB, 255, 255, 255)
        flower(radius=flower_radius, count=120,
               petal=balloon_petal, petal_color=petal_color, pollen_color=pollen_color)
    noLoop()


def draw():
    pass
