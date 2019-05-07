# Day 07
from __future__ import division
import os
import random

base_filename = 'day_07'
extension = 'png'
filename_description = ''


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


def all_walls(maze_side):
    walls = set()
    for x in range(0, maze_side-1):
        for y in range(0, maze_side-1):
            if sqrt((x-maze_side/2)**2 + (y-maze_side/2)**2) >= 0.4*maze_side:
                continue
            else:
                walls.add(((x, y), (x, y+1)))
                walls.add(((x, y), (x+1, y)))
    return walls


random.seed(2)


side = 500
maze_side = 50
maze_scale = side / maze_side

# http://collection.mam.org/details.php?id=8007
red = color(183, 19, 0)
yellow = color(250, 209, 0)
blue = color(30, 63, 177)


def setup():
    size(side, side)
    strokeWeight(maze_scale//4*2+1)
    strokeCap(PROJECT)
    background(255)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    lines = list(all_walls(maze_side))
    random.shuffle(lines)
    for ((x1, y1), (x2, y2)) in lines[:floor(len(lines)*0.35)]:
        stroke(random.choice([red, yellow, blue]))
        line(
            maze_scale*(x1+0.5),
            maze_scale*(y1+0.5),
            maze_scale*(x2+0.5),
            maze_scale*(y2+0.5)
        )
    stroke(255)
    for x in range(maze_side):
        for y in range(maze_side):
            point(maze_scale*(x+0.5), maze_scale*(y+0.5))
