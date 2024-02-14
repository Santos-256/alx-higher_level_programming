#!/usr/bin/python3
# test_modified_rectangle.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for models/modified_rectangle.py.

Unittest classes:
    TestModifiedRectangle_instantiation - line 25
    TestModifiedRectangle_width - line 114
    TestModifiedRectangle_height - line 190
    TestModifiedRectangle_x - line 262
    TestModifiedRectangle_y - line 334
    TestModifiedRectangle_order_of_initialization - line 402
    TestModifiedRectangle_area - line 430
    TestModifiedRectangle_update_args - line 538
    TestModifiedRectangle_update_kwargs - line 676
    TestModifiedRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.base import Base
from models.modified_rectangle import ModifiedRectangle


class TestModifiedRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the ModifiedRectangle class."""

    def test_modified_rectangle_is_base(self):
        self.assertIsInstance(ModifiedRectangle(10, 2), Base)

    def test_modified_rectangle_no_args(self):
        with self.assertRaises(TypeError):
            ModifiedRectangle()

    def test_modified_rectangle_one_arg(self):
        with self.assertRaises(TypeError):
            ModifiedRectangle(1)

    def test_modified_rectangle_two_args(self):
        m_r1 = ModifiedRectangle(10, 2)
        m_r2 = ModifiedRectangle(2, 10)
        self.assertEqual(m_r1.id, m_r2.id - 1)

    def test_modified_rectangle_three_args(self):
        m_r1 = ModifiedRectangle(2, 2, 4)
        m_r2 = ModifiedRectangle(4, 4, 2)
        self.assertEqual(m_r1.id, m_r2.id - 1)

    def test_modified_rectangle_four_args(self):
        m_r1 = ModifiedRectangle(1, 2, 3, 4)
        m_r2 = ModifiedRectangle(4, 3, 2, 1)
        self.assertEqual(m_r1.id, m_r2.id - 1)

    def test_modified_rectangle_five_args(self):
        self.assertEqual(7, ModifiedRectangle(10, 2, 0, 0, 7).id)

    def test_modified_rectangle_more_than_five_args(self):
        with self.assertRaises(TypeError):
            ModifiedRectangle(1, 2, 3, 4, 5, 6)

    def test_modified_rectangle_width_private(self):
        with self.assertRaises(AttributeError):
            print(ModifiedRectangle(5, 5, 0, 0, 1).__width)

    def test_modified_rectangle_height_private(self):
        with self.assertRaises(AttributeError):
            print(ModifiedRectangle(5, 5, 0, 0, 1).__height)

    def test_modified_rectangle_x_private(self):
        with self.assertRaises(AttributeError):
            print(ModifiedRectangle(5, 5, 0, 0, 1).__x)

    def test_modified_rectangle_y_private(self):
        with self.assertRaises(AttributeError):
            print(ModifiedRectangle(5, 5, 0, 0, 1).__y)

    def test_modified_rectangle_width_getter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, m_r.width)

    def test_modified_rectangle_width_setter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        m_r.width = 10
        self.assertEqual(10, m_r.width)

    def test_modified_rectangle_height_getter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, m_r.height)

    def test_modified_rectangle_height_setter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        m_r.height = 10
        self.assertEqual(10, m_r.height)

    def test_modified_rectangle_x_getter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, m_r.x)

    def test_modified_rectangle_x_setter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        m_r.x = 10
        self.assertEqual(10, m_r.x)

    def test_modified_rectangle_y_getter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, m_r.y)

    def test_modified_rectangle_y_setter(self):
        m_r = ModifiedRectangle(5, 7, 7, 5, 1)
        m_r.y = 10
        self.assertEqual(10, m_r.y)


class TestModifiedRectangle
