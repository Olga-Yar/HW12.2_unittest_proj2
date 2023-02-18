import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_get_negative(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_slice_empty(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])

    def test_slice_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1), [4])

    def test_slice_less_length_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5), [1, 2, 3, 4])
