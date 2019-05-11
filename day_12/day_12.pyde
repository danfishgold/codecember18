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


def color_from_hex(hex, sat=0, val=0):
    r, g, b = scaffold.hex_to_rgb(hex)
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    r2, g2, b2 = colorsys.hsv_to_rgb(h, s+sat, v+val)
    return color(r2*255, g2*255, b2*255)


# https://www.redblobgames.com/maps/terrain-from-noise/
OCEAN = color_from_hex("43437A", val=0.2)
SNOW = color_from_hex("DEDEE5")
DESERT = color_from_hex("D2B98B", sat=0.5, val=0.1)
FOREST = color_from_hex("337755", sat=0.5, val=0.1)


def biome(elevation, moisture, latitude, water):
    if elevation < water:
        return OCEAN

    desert_forest = lerpColor(DESERT,
                              FOREST,
                              moisture)

    ice_factor = (exp(4-4*latitude)*latitude**4)
    min_elevation_for_ice = ice_factor ** 0.15
    if ice_factor == 0:
        return SNOW
    else:
        if elevation > min_elevation_for_ice:
            return SNOW
        else:
            return lerpColor(desert_forest, SNOW, 0.5*elevation/min_elevation_for_ice)


side = 500


def setup():
    size(side, side)


random.seed(1)


def draw_():
    seed = random.randint(1, 10000)
    noiseSeed(seed)
    noise_scale = 0.02 / (side/500)
    noiseDetail(8, 0.65)

    elevation = [[noise(x * noise_scale, y * noise_scale)
                  for y in range(side)]
                 for x in range(side)]

    moisture = [[noise(100 + x * noise_scale, 100 + y * noise_scale)
                 for y in range(side)]
                for x in range(side)]

    for x in range(side):
        for y in range(side):
            if (x-width/2)**2 + (y-height/2)**2 <= (0.4*side)**2:
                elevation = noise(x * noise_scale, y * noise_scale)
                moisture = noise(10 + x * noise_scale, 10 + y * noise_scale)
                latitude = 1 - abs(y-side/2) / (side/2)
                stroke(biome(elevation, moisture, latitude, water=0.7))
                point(x, y)
