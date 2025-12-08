#!/usr/bin/python3
"""Unittest for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_single_element(self):
        self.assertEqual(max_integer([8]), 8)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 2, 9, 1]), 9)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 3, 1, 2]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 10, 5]), 10)

    def test_list_at_beginning(self):
        self.assertEqual(max_integer([99, 1, 2, 3]), 99)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 3])
