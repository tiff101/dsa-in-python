# to assert given conditions of each Euler problem.
import unittest
from problems_and_solutions import *


class BaseEuler(unittest.TestCase):
    def test_lattice_paths_15(self):

        grid_size = 2
        calculated_routes = lattice_paths_15(2)
        self.assertEqual(calculated_routes, 6)


if __name__ == '__main__':
    unittest.main()
