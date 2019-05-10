# Day ##
from __future__ import division
import scaffold


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_##',
        extension='png'
    )


side = 500


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
    ellipse(width/2, height/2, side*0.8, side*0.8)
