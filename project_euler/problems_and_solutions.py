"""
This file exists for the purpose of documenting all of Project Euler probs and solutions. 
Going at a slow pace so we'll see if and how this actually works. 
"""
import math

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


def special_pythagorean_triplet(abc_sum=1000):
    """
    https://projecteuler.net/problem=9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    :param abc_sum: natural number
    :return: a*b*c
    """

    # 1. find highest possible c squared value - break at 1000 and save
    for c in range(5, 100):
        c_squared = c ** 2
        if c_squared > 1000:
            break
    largest_c = c - 1
    print(largest_c)

    # 2. Now that you have a c limit, find all pythagorean triplets
    pythagorean_triplets = []
    for a in range(1, largest_c):
        # print("a", a)
        b = a + 1
        a_squared_plus_b_squared = a**2 + b**2
        print(f"a={a} b={b} a2+b2={a_squared_plus_b_squared}")

        if a_squared_plus_b_squared == largest_c**2:
            pythagorean_triplets.append([a, b, largest_c])




            # 3. Identify the triplet that satisfies sum of 1000

    # 4. Return product
