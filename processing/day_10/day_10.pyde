# Day 10: Tsuro
from __future__ import division
import os
import random

base_filename = 'day_10'
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


def point_from_index(x0, y0, tile_side, idx):
    if idx == 0:
        return (x0, y0+tile_side/3)
    if idx == 1:
        return (x0, y0+tile_side*2/3)
    if idx == 2:
        return (x0+tile_side/3, y0+tile_side)
    if idx == 3:
        return (x0+tile_side*2/3, y0+tile_side)
    if idx == 4:
        return (x0+tile_side, y0+tile_side*2/3)
    if idx == 5:
        return (x0+tile_side, y0+tile_side/3)
    if idx == 6:
        return (x0+tile_side*2/3, y0)
    if idx == 7:
        return (x0+tile_side/3, y0)


def normal_at_index(idx, multiplier=1):
    side = idx // 2
    if side == 0:
        return (multiplier, 0)
    elif side == 1:
        return (0, -multiplier)
    elif side == 2:
        return (-multiplier, 0)
    else:
        return (0, multiplier)


def relative_bezier(p1, n1, p2, n2):
    x1, y1 = p1
    x2, y2 = x1 + n1[0], y1 + n1[1]
    x4, y4 = p2
    x3, y3 = x4 + n2[0], y4 + n2[1]
    bezier(x1, y1, x2, y2, x3, y3, x4, y4)


def multipliers(i1, i2):
    if i1 % 2 == 1:
        diff = (i2 - i1) % 8
    else:
        diff = (i1 - i2) % 8

    if diff == 1:
        return (1/6, 1/6)
    elif diff == 2:
        return (1/3, 1/3)
    elif diff == 3:
        return (0, 0)
    elif diff == 4:
        return (1/2, 1/2)
    elif diff == 5:
        return (1/2.5, 1/2.5)
    elif diff == 6:
        return (1/3, 1/3)
    elif diff == 7:
        return (1/4.5, 1/4.5)
    else:
        raise ValueError("Bad indexes {} and {}".format(i1, i2))


def path(x0, y0, tile_side, i1, i2, stroke_color):
    p1 = point_from_index(x0, y0, tile_side, i1)
    p2 = point_from_index(x0, y0, tile_side, i2)
    m1, m2 = multipliers(i1, i2)
    n1 = normal_at_index(i1, m1*tile_side)
    n2 = normal_at_index(i2, m2*tile_side)
    strokeWeight(11*side//1000)
    stroke(0, 0, 1)
    strokeCap(SQUARE)
    relative_bezier(p1, n1, p2, n2)
    strokeWeight(5*side//1000)
    stroke(stroke_color)
    strokeCap(PROJECT)
    relative_bezier(p1, n1, p2, n2)


def tile(xc, yc, tile_side, paths):
    third = tile_side/3
    x0, y0 = xc - tile_side/2, yc - tile_side/2
    strokeWeight(2*side//1000)
    noFill()
    for (i1, i2, stroke_color) in paths:
        path(x0, y0, tile_side, i1, i2, stroke_color)
    # stroke(0, 0, 0)
    # rect(x0, y0, tile_side, tile_side)


def randomized_paths(indexes, stroke_color=color(0)):
    random.shuffle(indexes)
    half = len(indexes) // 2
    paths = zip(indexes[:half], indexes[half:], [stroke_color]*half)
    return paths


def opposite(row, col, idx):
    # adjecent tiles share points. This gives the index of the point in the other tile
    if idx == 0:
        return (row, col-1, 5)
    elif idx == 1:
        return (row, col-1, 4)
    elif idx == 2:
        return (row+1, col, 7)
    elif idx == 3:
        return (row+1, col, 6)
    elif idx == 4:
        return (row, col+1, 1)
    elif idx == 5:
        return (row, col+1, 0)
    elif idx == 6:
        return (row-1, col, 3)
    elif idx == 7:
        return (row-1, col, 2)


side = 2000


def rgb_from_hex(string):
    h = string.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def setup():
    size(side, side)
    colorMode(HSB, 1)
    background(0, 0, 1)


def mouseClicked():
    redraw()


def draw():
    background(0, 0, 1)
    draw_()
    noLoop()


# http://tools.medialab.sciences-po.fr/iwanthue/
colors = [
    color(208, 71, 153),
    color(97, 184, 94),
    color(169, 95, 201),
    color(183, 171, 65),
    color(113, 121, 203),
    color(198, 123, 66),
    color(77, 180, 192),
    color(205, 73, 73),
    color(97, 127, 63),
    color(190, 106, 141),
]

random.seed(1)


def draw_():
    seed = 9150  # random.randint(1, 100000)
    random.seed(seed)
    print 'seed', seed
    tile_count = 7
    tile_side = side / tile_count

    point_paths = dict()
    for row in range(tile_count):
        for col in range(tile_count):
            indexes = list(range(8))
            if col == 0:
                indexes.remove(0)
                indexes.remove(1)
            elif col == tile_count-1:
                indexes.remove(4)
                indexes.remove(5)
            if row == 0:
                indexes.remove(6)
                indexes.remove(7)
            elif row == tile_count-1:
                indexes.remove(2)
                indexes.remove(3)
            for (i1, i2, _) in randomized_paths(indexes):
                point_paths[(row, col, i1)] = (row, col, i1, i2)
                point_paths[(row, col, i2)] = (row, col, i2, i1)

    loops = []
    while point_paths:
        og_pt = list(point_paths.keys())[0]
        unvisited_loop_points = {og_pt}
        loop_paths = []
        while unvisited_loop_points:
            pt = unvisited_loop_points.pop()
            if pt in point_paths:
                row, col, i, j = point_paths.pop(pt)
                point_paths.pop((row, col, j))
                unvisited_loop_points.update([
                    opposite(row, col, i),
                    (row, col, j),
                    opposite(row, col, j)])
                loop_paths.append((row, col, i, j))
        loops.append(loop_paths)

    num_paths = 4*tile_count*(tile_count-1)
    if max(map(len, loops)) > 0.3*num_paths:
        draw_()
        return

    all_paths = []
    random.shuffle(colors)
    for paths, c in zip(loops, colors):
        # c = color((random.random() + index/len(loops)) % 1, 0.95, 0.8)
        for (row, col, i, j) in paths:
            all_paths.append((row, col, i, j, c))

    random.shuffle(all_paths)
    for (row, col, i, j, c) in all_paths:
        tile(
            tile_side/2 + tile_side*col,
            tile_side/2 + tile_side*row,
            tile_side,
            [(i, j, c)])
