# Day 12
from __future__ import division
import scaffold
import colorsys
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_12',
        extension='png'
    )


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def color_from_hex(hex):
    r, g, b = scaffold.hex_to_rgb(hex)
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    r2, g2, b2 = colorsys.hsv_to_rgb(h, s+0.3, v+0.1)
    return color(r2*255, g2*255, b2*255)


# https://www.astellescolors.com/2016/11/26/steep-coast/
# https://colorzilla.com/gradient-editor/#002c59+0,005f84+32,299f94+37,809f55+40,3a8235+56,2e723c+70,b3ae77+78,cfb59f+100
terrain_gradient = [
    (0, color_from_hex("002C59")),
    (0.30, color_from_hex("005F84")),
    (0.37, color_from_hex("299f94")),
    (0.40, color_from_hex("809f55")),
    (0.56, color_from_hex("3a8235")),
    (0.70, color_from_hex("2e723c")),
    (0.78, color_from_hex("b3ae77")),
    (1, color_from_hex("cfb59f")),
]


def color_gradient(f):
    index = 0
    f = min(1, max(0, f))
    while f > terrain_gradient[index+1][0]:
        index += 1
    f1, c1 = terrain_gradient[index]
    f2, c2 = terrain_gradient[index+1]
    ff = (f-f1) / (f2-f1)
    return lerpColor(c1, c2, ff)


side = 500


def setup():
    size(side, side)


random.seed(1)


def draw_():
    noiseSeed(random.randint(1, 10000))
    noise_scale = 0.02
    noiseDetail(4, 0.5)

    # ellipse(width/2, height/2, side*0.8, side*0.8)
    for x in range(0, side):
        for y in range(0, side):
            noise_value = noise(x * noise_scale, y * noise_scale)
            stroke(color_gradient(noise_value))
            point(x, y)
