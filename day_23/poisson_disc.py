# from https://scipython.com/blog/poisson-disc-sampling-in-python/

from math import cos, sin, pi, sqrt
import random


def get_cell_coords(pt, a):
    """Get the coordinates of the cell that pt = (x,y) falls in."""

    return int(pt[0] // a), int(pt[1] // a)


def get_neighbours(coords, cells, nx, ny):
    """Return the indexes of points in cells neighbouring cell at coords.

    For the cell at coords = (x,y), return the indexes of points in the cells
    with neighbouring coordinates illustrated below: ie those cells that could 
    contain points closer than r.

                                     ooo
                                    ooooo
                                    ooXoo
                                    ooooo
                                     ooo

    """

    dxdy = [(-1, -2), (0, -2), (1, -2), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
            (-2, 0), (-1, 0), (1, 0), (2, 0), (-2,
                                               1), (-1, 1), (0, 1), (1, 1), (2, 1),
            (-1, 2), (0, 2), (1, 2), (0, 0)]
    neighbours = []
    for dx, dy in dxdy:
        neighbour_coords = coords[0] + dx, coords[1] + dy
        if not (0 <= neighbour_coords[0] < nx and
                0 <= neighbour_coords[1] < ny):
            # We're off the grid: no neighbours here.
            continue
        neighbour_cell = cells[neighbour_coords]
        if neighbour_cell is not None:
            # This cell is occupied: store this index of the contained point.
            neighbours.append(neighbour_cell)
    return neighbours


def point_valid(pt, samples, cells, r, a, nx, ny):
    """Is pt a valid point to emit as a sample?

    It must be no closer than r from any other point: check the cells in its
    immediate neighbourhood.

    """

    cell_coords = get_cell_coords(pt, a)
    for idx in get_neighbours(cell_coords, cells, nx, ny):
        nearby_pt = samples[idx]
        # Squared distance between or candidate point, pt, and this nearby_pt.
        distance2 = (nearby_pt[0]-pt[0])**2 + (nearby_pt[1]-pt[1])**2
        if distance2 < r**2:
            # The points are too close, so pt is not a candidate.
            return False
    # All points tested: if we're here, pt is valid
    return True


def get_point(k, refpt, samples, cells, r, a, nx, ny):
    """Try to find a candidate point relative to refpt to emit in the sample.

    We draw up to k points from the annulus of inner radius r, outer radius 2r
    around the reference point, refpt. If none of them are suitable (because
    they're too close to existing points in the sample), return False.
    Otherwise, return the pt.

    """
    i = 0
    while i < k:
        rho, theta = random.uniform(r, 2*r), random.uniform(0, 2*pi)
        pt = refpt[0] + rho*cos(theta), refpt[1] + rho*sin(theta)

        if (pt[0]-0.5)**2 + (pt[1]-0.5)**2 >= 0.4**2:
            # This point falls outside the domain, so try again.
            continue
        if point_valid(pt, samples, cells, r, a, nx, ny):
            return pt
        i += 1
    # We failed to find a suitable point in the vicinity of refpt.
    return False


def sample(initial_set, r=0.05, k=30):
    # k: Choose up to k points around each reference point as candidates for a new
    # sample point
    # r: Minimum distance between samples

    # Cell side length
    a = r/sqrt(2)
    # Number of cells in the x- and y-directions of the grid
    nx, ny = int(1 / a) + 1, int(1 / a) + 1

    # A list of coordinates in the grid of cells
    coords_list = [(ix, iy) for ix in range(nx) for iy in range(ny)]
    # Initilalize the dictionary of cells: each key is a cell's coordinates, the
    # corresponding value is the index of that cell's point's coordinates in the
    # samples list (or None if the cell is empty).
    cells = {coords: None for coords in coords_list}

    samples = initial_set
    for idx, pt in enumerate(initial_set):
        cells[get_cell_coords(pt, a)] = idx
    active = list(range(len(initial_set)))

    # As long as there are points in the active list, keep trying to find samples.
    while active:
        # choose a random "reference" point from the active list.
        idx = random.choice(active)
        refpt = samples[idx]
        # Try to pick a new point relative to the reference point.
        pt = get_point(k, refpt, samples, cells, r, a, nx, ny)
        if pt:
            # Point pt is valid: add it to the samples list and mark it as active
            samples.append(pt)
            active.append(len(samples)-1)
            cells[get_cell_coords(pt, a)] = len(samples) - 1
        else:
            # We had to give up looking for valid points near refpt, so remove it
            # from the list of "active" points.
            active.remove(idx)

    return samples