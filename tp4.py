import numpy as np
import cmath  


def generate_infinite_curve(nombre_points):
    t = np.linspace(0, 2 * np.pi, nombre_points)
    x_points = []
    y_points = []
    L = []

    for angle in t:
        x = np.sin(angle)
        y = np.cos(angle) * np.sin(angle)
        x_points.append(x)
        y_points.append(y)
        L.append((x, y))

    return L

def generate_grid_points(n):
    grid = []
    for i in range(n):
        for j in range(n):
            grid.append((i, j))
    return grid


def generate_concentric_circles_points(nombre_points):
    def cercle_unite(rayon, nombre_points):
        points_cercle = []
        for k in range(nombre_points):
            z = cmath.exp(2j * cmath.pi * k / nombre_points)
            x = rayon * z.real
            y = rayon * z.imag
            points_cercle.append((x, y))
        return points_cercle

    rayon_petit = 10
    rayon_grand = 20

    points_petit_cercle = cercle_unite(rayon_petit, nombre_points)
    points_grand_cercle = cercle_unite(rayon_grand, nombre_points)

    return points_petit_cercle + points_grand_cercle





