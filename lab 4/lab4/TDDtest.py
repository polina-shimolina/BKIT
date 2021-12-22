import main
import unittest
from unittest.mock import patch


class Tests(unittest.TestCase):
    def test_2(self):
        roots = main.check_coef(1, -4, 4)
        self.assertAlmostEqual(1.4142, roots[0], 4)
        self.assertAlmostEqual(-1.4142, roots[1], 4)

    def test_3(self):
        roots = main.check_coef(-4, 16, 0)
        self.assertEqual([0, 2, -2], roots)

    def test_4(self):
        roots = main.check_coef(1, -10, 9)
        self.assertEqual([3, -3, 1, -1], roots)

    def test_0(self):
        roots = main.check_coef(1, 0, 10)
        self.assertEqual([], roots)

    def test_inf(self):
        roots = main.check_coef(0, 0, 0)
        self.assertEqual(['infinity'], roots)

    @patch('main.check_coef', return_value=[9])
    def test_m(self, check_coef):
        self.assertEqual(main.check_coef(1, 2, 3), [9])
