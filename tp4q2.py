import math
import random
import matplotlib.pyplot as plt
from tp4 import *
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** m + (y1 - y2) ** m)**1/m

def calculate_cost(grid, route, coordinates):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance(coordinates[route[i]][0], coordinates[route[i]][1],
                         coordinates[route[i + 1]][0], coordinates[route[i + 1]][1])
    return cost

def metropolis_hastings(grid, route, coordinates, temperature, iteration):
    current_cost = calculate_cost(grid, route, coordinates)
    best_cost = current_cost
    best_route = route

    for _ in range(iteration):
        neighbour_route = generate_neighbour(route, coordinates)
        neighbour_cost = calculate_cost(grid, neighbour_route, coordinates)

        # Calculer la probabilité d'acceptation
        acceptance_prob = min(1, math.exp((current_cost - neighbour_cost) / temperature))

        # Accepter la nouvelle solution avec une probabilité donnée
        if random.random() < acceptance_prob:
            current_cost = neighbour_cost
            route = neighbour_route

        # Mettre à jour la meilleure solution trouvée jusqu'à présent
        if current_cost < best_cost:
            best_cost = current_cost
            best_route = route

    return best_cost, best_route

def generate_neighbour(route, coordinates):
    neighbour_route = route[:]
    i, j = random.sample(range(len(route)), 2)
    neighbour_route[i], neighbour_route[j] = neighbour_route[j], neighbour_route[i]
    return neighbour_route

def plot_solution(coordinates, route, grid_points):
    route_coordinates = [coordinates[i] for i in route]

    x = [coord[0] for coord in route_coordinates]
    y = [coord[1] for coord in route_coordinates]

    optimal_route = list(zip(x, y))  # Convertir les coordonnées en tuples

    plt.scatter([point[0] for point in grid_points], [point[1] for point in grid_points], color='g', label='Grid Points')
    plt.plot(x, y, marker='.', linestyle='-', color='b', label='Optimal Route')
    plt.scatter(x, y, color='r', label='Cities')
    plt.title('Optimal Route and Cities on the Grid')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.show()

    return optimal_route


def main():
    n = 10

    grid_points = generate_grid_points(n)
    random.shuffle(grid_points)

    grid = generate_grid_points(n)
    route = list(range(len(grid_points)))
    coordinates = grid_points
    temperature = 1000.0
    iteration = 1000

    cost, route = metropolis_hastings(grid, route, coordinates, temperature, iteration)

    print("Minimum cost:", cost)
    plot_solution(coordinates, route, grid_points)

if __name__ == "__main__":
    n = 50
    m= 2
    grid_points = generate_grid_points(n)
    random.shuffle(grid_points)

    grid = generate_grid_points(n)
    route = list(range(len(grid_points)))
    coordinates = grid_points
    temperature = 1000.0
    iteration = 1000

    cost, route = metropolis_hastings(grid, route, coordinates, temperature, iteration)

    print("Minimum cost:", cost)
    optimal_route = plot_solution(coordinates, route, grid_points)
    print("Optimal route (coordinates):", optimal_route)


