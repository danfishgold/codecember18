# Day 11: Blokus
from __future__ import division
import scaffold
import random


def keyPressed():
    scaffold.image_saving_key_event_handler(
        base_filename='day_11',
        extension='png'
    )


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


def forbidden_points(points):
    return (points
            .union(shift(points, 1, 0))
            .union(shift(points, -1, 0))
            .union(shift(points, 0, 1))
            .union(shift(points, 0, -1)))


def draw_shape(shape, color):
    fill(color)
    for (x, y) in shape:
        rect(x*square_side, y*square_side, square_side, square_side)


def draw_board():
    strokeWeight(side // 500 // 2 * 2 + 1)
    stroke(0)
    for rowcol in range(square_count+1):
        line(0, square_side*rowcol, side, square_side*rowcol)
        line(square_side*rowcol, 0, square_side*rowcol, side)


def is_point_valid(x, y, taken_points, square_count):
    return ((0 <= x < square_count)
            and (0 <= y < square_count)
            and (x, y) not in forbidden_points(taken_points))


def is_shape_valid(shape, taken_points, square_count):
    return all((is_point_valid(x, y, taken_points, square_count) for (x, y) in shape))


side = 500
square_count = 20
square_side = side/square_count

square1 = {(0, 0)}
square2 = {(0, 0), (1, 0), (0, 1), (1, 1)}
line2 = {(0, 0), (0, 1)}
line3 = {(0, 0), (0, 1), (0, 2)}
line4 = {(0, 0), (0, 1), (0, 2), (0, 3)}
line5 = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
corner22 = {(0, 0), (1, 0), (0, 1)}
corner23 = {(0, 0), (1, 0), (0, 1), (0, 2)}
corner24 = {(0, 0), (1, 0), (0, 1), (0, 2), (0, 3)}
corner33 = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)}
plus23 = {(0, 0), (0, 1), (0, 2), (1, 1)}
plus33 = {(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)}

shapes = [square1, square2,
          line2, line3, line4, line5,
          corner22, corner23, corner24, corner33,
          plus23, plus33]
# shapes = [line2]

all_shapes_rotatations = [[], [], [], []]
for shape in shapes:
    for n in range(4):
        all_shapes_rotatations[n].extend(all_corner_arrangements(shape, n))


def setup():
    size(side, side)


def mouseClicked():
    redraw()


def draw():
    background(255)
    draw_()
    noLoop()


class Player:
    def __init__(self):
        self.points = set()
        self.forbidden_points = set()
        self.next_origins = set()

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


class Game:
    def __init__(self, player_count, square_count):
        self.square_count = square_count

        if player_count == 1:
            seeds = [(0, 0)]

        elif player_count == 2:
            seeds = [
                (0, 0),
                (square_count-1, square_count-1)
            ]

        else:
            seeds = [
                (0, 0),
                (0, square_count-1),
                (square_count-1, 0),
                (square_count-1, square_count-1)
            ]

        self.players = []
        self.all_points = set()
        for seed in seeds:
            player = Player()
            self.players.append(player)
            self.add_points_to_player({seed}, player)

    def turn(self, player):

        while not player.is_finished():
            x, y, n = player.pop_possible_origin()

            options = []
            for candidate in all_shapes_rotatations[(n-2) % 4]:
                if self.shape_fits(player, candidate, x, y):
                    options.append(shift(candidate, x, y))

            if options:
                self.add_points_to_player(random.choice(options), player)
                return True
        return False

    def round(self):
        turns = [self.turn(player) for player in self.players]
        return all(turns)

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


def is_point_in_bounds(pt, square_count):
    return (0 <= pt[0] < square_count) and (0 <= pt[1] < square_count)


random.seed(2)

seed = random.randint(1, 10000)
print seed
random.seed(seed)


def draw_():

    draw_board()

    game = Game(2, square_count)

    while game.round():
        pass
    draw_shape(game.players[1].points, color(255, 0, 0))
    draw_shape(game.players[0].points, color(0, 255, 0))
