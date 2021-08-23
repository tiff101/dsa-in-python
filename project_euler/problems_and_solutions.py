"""
This file exists for the purpose of documenting all of Project Euler probs and solutions. 
Going at a slow pace so we'll see if and how this actually works. 
"""


def lattice_paths_15(grid_size):
    """
    https://projecteuler.net/problem=15
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
    :param int grid_size: one side of a square grid.
    """
    num_right_down_moves = grid_size * 2
    routes = num_right_down_moves + 2 ** (grid_size - 1)
    return routes
