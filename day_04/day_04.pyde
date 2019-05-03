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
# https://www.gardenia.net/rendition.slider_detail/uploads/plant/1523279216-de1e281688b782541/Garden_Mum_Cheryl_Pink_Bloom_13449Optimized.jpg
petal_color = color(182, 72, 138)
pollen_color = color(190, 120, 90)
white = color(255)

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


def flower_petals(petal, base_color, base_length, base_width, count):
    dtheta = TWO_PI/phi
    for i in range(count)[::-1]:
        f = i/count
        theta = i*dtheta
        color = serp_color(base_color, white, lerp(
            0, 0.8, f+randomGaussian()*0.03))
        length = base_length * serp(0.13, 1, f+randomGaussian()*0.01)
        width = base_width * serp(0.2, 1, f+randomGaussian()*0.03)
        fill(color)
        petal(theta, length, width)


def pollen(color, center_radius, pollen_radius, count):
    fill(color)
    stroke(0)
    strokeWeight(1)
    for _ in range(count):
        r = random(0, center_radius/2)
        theta = random(0, TWO_PI)
        ellipse(r*cos(theta), r*sin(theta), pollen_radius, pollen_radius)


def flower(petal, petal_color, pollen_color, length, width, center_radius, count):
    stroke(0)
    flower_petals(petal, petal_color, length, width, count)
    pollen(pollen_color, center_radius, center_radius/4, 80)


def setup():

    size(side, side)
    strokeWeight(ceil(side/800))
    background(255)
    stroke(0)

    translate(width/2, height/2)
    flower(balloon_petal, petal_color=petal_color, pollen_color=pollen_color,
           length=side/4, width=side/10, center_radius=side/40, count=120)

    noLoop()


def draw():
    pass