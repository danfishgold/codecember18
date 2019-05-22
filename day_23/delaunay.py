from collections import Counter


def is_point_in_triange_circumcircle(pt, ccw_triangle):
    (ax, ay), (bx, by), (cx, cy) = ccw_triangle
    px, py = pt
    dax = ax-px
    day = ay-py
    dbx = bx-px
    dby = by-py
    dcx = cx-px
    dcy = cy-py
    determinant = (
        (dax*dax + day*day) * (dbx*dcy-dcx*dby) -
        (dbx*dbx + dby*dby) * (dax*dcy-dcx*day) +
        (dcx*dcx + dcy*dcy) * (dax*dby-dbx*day)
    )
    return determinant > 0


def is_counter_clockwise(triangle):
    (ax, ay), (bx, by), (cx, cy) = triangle
    return (bx - ax)*(cy - ay)-(cx - ax)*(by - ay) > 0


def make_ccw(triangle):
    if not is_counter_clockwise(triangle):
        return (triangle[0], triangle[2], triangle[1])
    else:
        return triangle


def sort_edge(edge):
    (x1, y1), (x2, y2) = edge
    if x1 < x2 or (x1 == x2 and y1 <= y1):
        return ((x1, y1), (x2, y2))
    else:
        return ((x2, y2), (x1, y1))


def sorted_edges(triangle):
    return map(sort_edge, (
        (triangle[0], triangle[1]),
        (triangle[1], triangle[2]),
        (triangle[2], triangle[0])
    ))


class Triangulation:
    def __init__(self, super_triangle):
        self.super_triangle_vertexes = set(super_triangle)
        self.triangulation = {make_ccw(super_triangle)}

    def add_point(self, pt):
        bad_triangles = set()
        for triangle in self.triangulation:
            if is_point_in_triange_circumcircle(pt, triangle):
                bad_triangles.add(triangle)
        bad_triangle_edge_count = Counter(edge
                                          for triangle in bad_triangles
                                          for edge in sorted_edges(triangle)
                                          )
        polygon_edges = set()
        for triangle in bad_triangles:
            for edge in sorted_edges(triangle):
                if bad_triangle_edge_count[edge] == 1:
                    polygon_edges.add(edge)
            self.triangulation.remove(triangle)

        for p1, p2 in polygon_edges:
            tri = (p1, p2, pt)
            self.triangulation.add(make_ccw(tri))

    def in_super_triangle(self, triangle):
        return any(vertex in self.super_triangle_vertexes for vertex in triangle)

    def triangles(self):
        return filter(lambda tri: not self.in_super_triangle(tri), self.triangulation)
