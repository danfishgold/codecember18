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


def prim_step(maze_points, wall_set, passage_set, wd, ht):
    wall = random.sample(wall_set, 1)[0]
    wall_set.remove(wall)
    # wall = wall_set.pop() # This isn't truly random
    pt1, pt2 = wall
    pt1_visited = pt1 in maze_points
    pt2_visited = pt2 in maze_points
    if pt1_visited and not pt2_visited:
        new_pt = pt2
    elif not pt1_visited and pt2_visited:
        new_pt = pt1
    else:
        return None

    maze_points.add(new_pt)
    passage_set.add(wall)
    wall_set.update(neighboring_walls(new_pt, passage_set, wd, ht))
    return wall


def neighboring_walls(pt, passage_set, wd, ht):
    x, y = pt
    walls = []
    if x >= 1:
        walls.append(((x-1, y), (x, y)))
    if y >= 1:
        walls.append(((x, y-1), (x, y)))
    if x < wd-1:
        walls.append(((x, y), (x+1, y)))
    if y < ht-1:
        walls.append(((x, y), (x, y+1)))
    return list(filter(lambda wall: wall not in passage_set, walls))


side = 500
wd = side/10
ht = side/10
center = (wd//2, ht//2)
corners = [(0, 0), (0, ht-1), (wd-1, 0), (wd-1, ht-1)]
maze_points = {center}
passage_set = set()
wall_set = {wall
            for pt in maze_points
            for wall in neighboring_walls(pt, passage_set, wd, ht)}


def setup():
    size(side, side)
    strokeWeight(5)
    background(255)
    stroke(0)


def mouseClicked():
    redraw()


def draw():
    draw_()


def draw_():
    if wall_set:
        new_passage = prim_step(maze_points, wall_set, passage_set, wd, ht)
        if new_passage:
            ((x1, y1), (x2, y2)) = new_passage
            line(5+10*x1, 5+10*y1, 5+10*x2, 5+10*y2)
    else:
        noLoop()
