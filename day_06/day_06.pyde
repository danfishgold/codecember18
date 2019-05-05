# Day 06
from __future__ import division
import os
import random

base_filename = 'day_06'
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


side = 500


def prim_step(maze_points, wall_list, passage_set):
    wall_index = random.randint(0, len(wall_list)-1)
    wall = wall_list.pop(wall_index)
    pt1, pt2 = wall
    if pt1 in maze_points and not pt2 in maze_points:
        new_pt = pt2
    elif pt1 not in maze_points and pt2 in maze_points:
        new_pt = pt1
    else:
        return (maze_points, wall_list, passage_set)

    maze_points.add(new_pt)
    passage_set.add(wall)
    wall_list.extend(neighboring_walls(new_pt, passage_set))
    return (maze_points, wall_list, passage_set)


def neighboring_walls(pt, passage_set):
    x, y = pt
    walls = []
    if x >= 1:
        walls.append(((x-1, y), (x, y)))
    if y >= 1:
        walls.append(((x, y-1), (x, y)))
    if x < 50:
        walls.append(((x, y), (x+1, y)))
    if y < 50:
        walls.append(((x, y), (x, y+1)))
    return list(filter(lambda wall: wall not in passage_set, walls))


maze_points, wall_list, passage_set = {
    (0, 0)}, [((0, 0), (0, 1)), ((0, 0), (1, 0))], set()


def setup():
    size(side, side)
    strokeWeight(ceil(side/500))
    background(255)
    stroke(0)

    while wall_list:
        prim_step(maze_points, wall_list, passage_set)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def draw_():
    for ((x1, y1), (x2, y2)) in passage_set:
        line(8*(x1+1), 8*(y1+1), 8*(x2+1), 8*(y2+1))
