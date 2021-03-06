# Day 06: Maze Complement
from __future__ import division
import os
import random

base_filename = 'day_06'
extension = 'png'
filename_description = ''

random.seed(2)


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


def prim_step(maze_points, passage_set, wall_set, maze_side):
    potential_wall = random.sample(passage_set, 1)[0]
    passage_set.remove(potential_wall)
    # potential_wall = passage_set.pop() # This isn't truly random
    pt1, pt2 = potential_wall
    pt1_visited = pt1 in maze_points
    pt2_visited = pt2 in maze_points
    if pt1_visited and not pt2_visited:
        new_pt = pt2
    elif not pt1_visited and pt2_visited:
        new_pt = pt1
    else:
        return None

    maze_points.add(new_pt)
    wall_set.add(potential_wall)
    passage_set.update(neighboring_passages(new_pt, wall_set, maze_side))


def neighboring_passages(pt, wall_set, maze_side):
    x, y = pt
    if sqrt((x-maze_side/2)**2 + (y-maze_side/2)**2) >= 0.4*maze_side:
        return []
    walls = []
    if x >= 1:
        walls.append(((x-1, y), (x, y)))
    if y >= 1:
        walls.append(((x, y-1), (x, y)))
    if x < maze_side-1:
        walls.append(((x, y), (x+1, y)))
    if y < maze_side-1:
        walls.append(((x, y), (x, y+1)))
    return list(filter(lambda wall: wall not in wall_set, walls))


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


side = 2000
maze_side = 77
maze_scale = side / maze_side
center = (maze_side//2, maze_side//2)
corners = [(0, 0), (0, maze_side-1), (maze_side-1, 0),
           (maze_side-1, maze_side-1)]


def setup():
    size(side, side)
    strokeWeight(maze_scale//4*2+1)
    background(255)
    stroke(0)


show_walls = False


def mouseClicked():
    global show_walls
    show_walls = not show_walls
    redraw()


def draw():
    draw_()
    noLoop()


maze_points = {center}
wall_set = set()
passage_set = {wall
               for pt in maze_points
               for wall in neighboring_passages(pt, wall_set, maze_side)}

while passage_set:
    prim_step(maze_points, passage_set, wall_set, maze_side)

passages = all_walls(maze_side).difference(wall_set)


def draw_():
    lines = wall_set if show_walls else passages
    background(255)
    for ((x1, y1), (x2, y2)) in lines:
        line(
            maze_scale*x1,
            maze_scale*y1,
            maze_scale*x2,
            maze_scale*y2
        )
