"""Tests for big_integer_nth_root."""

import unittest

from big_integer_nth_root import integer_nth_root


class TestIntegerNthRoot(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(integer_nth_root(0, 1), 0)
        self.assertEqual(integer_nth_root(1, 1), 1)
        self.assertEqual(integer_nth_root(0, 5), 0)
        self.assertEqual(integer_nth_root(1, 5), 1)

    def test_degree_one_returns_input(self):
        for n in (0, 1, 2, 10, 10**10, 10**100):
            self.assertEqual(integer_nth_root(n, 1), n)

    def test_exact_roots(self):
        self.assertEqual(integer_nth_root(4, 2), 2)
        self.assertEqual(integer_nth_root(27, 3), 3)
        self.assertEqual(integer_nth_root(16, 4), 2)
        self.assertEqual(integer_nth_root(10**10, 10), 10)

    def test_floor_roots(self):
        self.assertEqual(integer_nth_root(26, 3), 2)
        self.assertEqual(integer_nth_root(80, 4), 2)
        self.assertEqual(integer_nth_root(10**10 - 1, 10), 9)

    def test_large_arbitrary_precision(self):
        n = 12345678901234567890123456789012345678901234567890
        k = 17
        r = integer_nth_root(n, k)
        self.assertLessEqual(r ** k, n)
        self.assertGreater((r + 1) ** k, n)

    def test_initial_estimate_overshoot(self):
        # n just below a power of two; initial bit_length estimate can be
        # one too high.
        n = 2**30 - 1
        k = 3
        r = integer_nth_root(n, k)
        self.assertLessEqual(r ** k, n)
        self.assertGreater((r + 1) ** k, n)

    def test_invalid_degree(self):
        with self.assertRaises(ValueError):
            integer_nth_root(10, 0)
        with self.assertRaises(ValueError):
            integer_nth_root(10, -1)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            integer_nth_root(-1, 3)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            integer_nth_root(10.5, 2)
        with self.assertRaises(TypeError):
            integer_nth_root(10, 2.0)

    def test_huge_number_square_root(self):
        n = 10**200
        r = integer_nth_root(n, 2)
        self.assertEqual(r, 10**100)

    def test_huge_number_odd_degree(self):
        n = 10**201
        k = 3
        r = integer_nth_root(n, k)
        self.assertLessEqual(r ** k, n)
        self.assertGreater((r + 1) ** k, n)


if __name__ == "__main__":
    unittest.main()
