# Day 11: Blokus
from __future__ import division
import scaffold
import random
from collections import defaultdict


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


def shift(points, dx, dy):
    return {(dx+x, dy+y) for (x, y) in points}


def rotate(points, n, new_origin=(0, 0)):
    x0, y0 = new_origin
    n = n % 4
    if n == 0:
        def rotator(x, y): return (x, y)
    elif n == 1:
        def rotator(x, y): return (y, -x)
    elif n == 2:
        def rotator(x, y): return (-x, -y)
    elif n == 3:
        def rotator(x, y): return (-y, x)

    return {rotator(x-x0, y-y0) for (x, y) in points}


def rotation_direction(n):
    return (
        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1)
    )[n]


def all_corners(points):
    shifts = dict()
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            else:
                shifts[dx, dy] = {(x+dx, y+dy) for (x, y) in points}

    corners = [None, None, None, None]
    for n in range(4):
        dx, dy = rotation_direction(n)
        corners[n] = (points
                      .difference(shifts[dx, 0])
                      .difference(shifts[0, dy])
                      .difference(shifts[dx, dy])
                      )

    return corners


def all_corner_arrangements(points, n0):
    arrangements = set()
    for n, pts in enumerate(all_corners(points)):
        for (x0, y0) in pts:
            arrangements.add(tuple(sorted(rotate(points, n-n0, (x0, y0)))))
    return [set(arr) for arr in arrangements]


class Player:
    def __init__(self, origin, max_shape_uses=1):
        self.points = set()
        self.forbidden_points = set()
        self.next_origins = {origin}
        self.used_shapes = defaultdict(int)
        self.max_shape_uses = max_shape_uses

    def did_use_shape(self, shape_index):
        return self.used_shapes[shape_index] == self.max_shape_uses

    def mark_shape_as_used(self, shape_index):
        self.used_shapes[shape_index] += 1

    def add_points(self, pts, square_count):
        self.points.update(pts)
        self.next_origins.update(
            Player.corner_origins_in_bounds(pts, square_count))
        self.forbidden_points.update(pts)
        self.forbidden_points.update(shift(pts, 1, 0))
        self.forbidden_points.update(shift(pts, -1, 0))
        self.forbidden_points.update(shift(pts, 0, 1))
        self.forbidden_points.update(shift(pts, 0, -1))

    def is_finished(self):
        return len(self.next_origins) == 0

    def pop_possible_origin(self):
        origin = random.sample(self.next_origins, 1)[0]
        self.next_origins.remove(origin)
        return origin

    @staticmethod
    def corner_origins_in_bounds(points, square_count):
        return {(x, y, n)
                for (n, pts) in enumerate(all_corners(points))
                for (x, y) in shift(pts, *rotation_direction(n-2))
                if is_point_in_bounds((x, y), square_count)}

    def draw(self, color, square_side):
        fill(color)
        for (x, y) in self.points:
            rect(x*square_side, y*square_side, square_side, square_side)


class Game:
    def __init__(self, player_count, square_count, max_shape_uses=1):
        self.square_count = square_count

        if player_count == 1:
            seeds = [(0, 0, 2)]

        elif player_count == 2:
            seeds = [
                (0, 0, 2),
                (square_count-1, square_count-1, 0)
            ]

        else:
            seeds = [
                (0, 0, 2),
                (0, square_count-1, 1),
                (square_count-1, square_count-1, 0),
                (square_count-1, 0, 3)
            ]

        self.players = []
        self.all_points = set()
        for seed in seeds:
            player = Player(seed, max_shape_uses=max_shape_uses)
            self.players.append(player)

    def turn(self, player):

        while not player.is_finished():
            x, y, n = player.pop_possible_origin()

            options = []
            for shape_index, candidate in all_shapes_rotatations[(n-2) % 4]:
                if not player.did_use_shape(shape_index) and self.shape_fits(player, candidate, x, y):
                    options.append((shape_index, shift(candidate, x, y)))

            if options:
                max_size = max(map(lambda (_, shape): len(shape), options))
                options = filter(
                    lambda (_, shape): len(shape) == max_size,
                    options)
                shape_index, shape = random.choice(options)
                self.add_points_to_player(shape, player)
                player.mark_shape_as_used(shape_index)
                return True
        return False

    def round(self):
        turns = [self.turn(player) for player in self.players]
        return any(turns)

    def add_points_to_player(self, points, player):
        player.add_points(points, self.square_count)
        self.all_points.update(points)

    def shape_fits(self, player, shape, x0, y0):
        return all((self.point_fits(player, x0+x, y0+y) for (x, y) in shape))

    def point_fits(self, player, x, y):
        return (
            is_point_in_bounds((x, y), self.square_count)
            and (x, y) not in self.all_points
            and (x, y) not in player.forbidden_points
        )

    def draw(self, colors, side):
        square_side = side / self.square_count
        for player, color in zip(self.players, colors):
            player.draw(color, square_side)


def is_point_in_bounds(pt, square_count):
    return (0 <= pt[0] < square_count) and (0 <= pt[1] < square_count)


square1 = {(0, 0)}
square2 = {(0, 0), (1, 0), (0, 1), (1, 1)}
square21 = {(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)}
line2 = {(0, 0), (0, 1)}
line3 = {(0, 0), (0, 1), (0, 2)}
line4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
line5 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
corner22 = {(0, 0), (1, 0), (0, 1)}
corner23 = {(0, 0), (1, 0), (0, 1), (0, 2)}
corner24 = {(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)}
corner33 = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
kamatz23 = {(0, 0), (0, 1), (0, 2), (1, 1)}
kamatz24 = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)}
kamatz33 = {(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}
step222 = {(0, 0), (1, 0), (1, 1), (2, 1)}
step232 = {(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)}
step223 = {(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)}
step2222 = {(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)}
kaf = {(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)}
plus = {(0, 0), (0, 1), (0, 2), (1, 1), (-1, 1)}
weird_plus = {(0, 0), (0, 1), (0, 2), (-1, 1), (1, 2)}

shapes = [square1, square2, square21,
          line2, line3, line4, line5,
          corner22, corner23, corner24, corner33,
          kamatz23, kamatz24, kamatz33,
          step222, step232, step223, step2222,
          plus, weird_plus, kaf
          ]

all_shapes_rotatations = [[], [], [], []]
for shape_index, shape in enumerate(shapes):
    for n in range(4):
        arrangements = [(shape_index, arr)
                        for arr in all_corner_arrangements(shape, n)]
        all_shapes_rotatations[n].extend(arrangements)


player_colors = [
    color(0, 255, 0),
    color(255, 0, 0),
    color(0, 0, 255),
    color(255, 255, 0)
]

# https://coolors.co/931621-330c2f-595457-f0803c-f0803c
player_colors = [
    color(51, 12, 47),
    color(240, 128, 60),
    color(147, 22, 33),
    color(89, 84, 87)
]


side = 2000

random.seed(2)


def setup():
    size(side, side)


def draw_():
    seed = random.randint(1, 10000)
    print seed
    random.seed(seed)

    noStroke()

    scale = 1
    game = Game(
        player_count=4,
        square_count=20*scale,
        max_shape_uses=1*scale*scale
    )

    while game.round():
        pass

    game.draw(player_colors, side)
