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
    # h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    # r2, g2, b2 = colorsys.hsv_to_rgb(h, s+0.3, v+0.1)
    # return color(r2*255, g2*255, b2*255)
    return color(r, g, b)


# https://www.redblobgames.com/maps/terrain-from-noise/
OCEAN = color_from_hex("43437A")
BEACH = color_from_hex("9E8F77")
SCORCHED = color_from_hex("555555")
BARE = color_from_hex("888888")
TUNDRA = color_from_hex("BCBCAB")
SNOW = color_from_hex("DEDEE5")
TEMPERATE_DESERT = color_from_hex("C9D29B")
SHRUBLAND = color_from_hex("889977")
TAIGA = color_from_hex("99AB77")
GRASSLAND = color_from_hex("88AB55")
TEMPERATE_DECIDUOUS_FOREST = color_from_hex("679359")
TEMPERATE_RAIN_FOREST = color_from_hex("438855")
SUBTROPICAL_DESERT = color_from_hex("D2B98B")
TROPICAL_SEASONAL_FOREST = color_from_hex("569944")
TROPICAL_RAIN_FOREST = color_from_hex("337755")


def biome(temperature, moisture):
    if temperature < 0.1:
        return OCEAN
    if temperature < 0.12:
        return BEACH

    if temperature > 0.8:
        if moisture < 0.1:
            return SCORCHED
        if moisture < 0.2:
            return BARE
        if moisture < 0.5:
            return TUNDRA
        return SNOW

    if temperature > 0.6:
        if moisture < 0.33:
            return TEMPERATE_DESERT
        if moisture < 0.66:
            return SHRUBLAND
        return TAIGA

    if temperature > 0.3:
        if moisture < 0.16:
            return TEMPERATE_DESERT
        if moisture < 0.50:
            return GRASSLAND
        if moisture < 0.83:
            return TEMPERATE_DECIDUOUS_FOREST
        return TEMPERATE_RAIN_FOREST

    if moisture < 0.16:
        return SUBTROPICAL_DESERT
    if moisture < 0.33:
        return GRASSLAND
    if moisture < 0.66:
        return TROPICAL_SEASONAL_FOREST
    return TROPICAL_RAIN_FOREST


side = 500


def setup():
    size(side, side)


random.seed(1)


def draw_():
    noiseSeed(random.randint(1, 10000))
    noise_scale = 0.01 / (side/500)
    noiseDetail(8, 0.5)

    elevation = [[noise(x * noise_scale, y * noise_scale)
                  for y in range(side)]
                 for x in range(side)]

    moisture = [[noise(1000000 + x * noise_scale, 1000000 + y * noise_scale)
                 for y in range(side)]
                for x in range(side)]

    for x in range(side):
        for y in range(side):
            # if (x-width/2)**2 + (y-height/2)**2 <= (0.4*side)**2:
            e, m = elevation[x][y], moisture[x][y]
            stroke(biome(e**2, m**2))
            point(x, y)
