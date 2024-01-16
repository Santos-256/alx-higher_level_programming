#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCsv - line 404
    TestBaseLoadFromFileCsv - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    # Other test cases...

class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    # Test cases...

class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    # Test cases...

class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    # Test cases...

class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    # Test cases...

class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    # Test cases...

class TestBaseSaveToFileCsv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    # Test cases...

class TestBaseLoadFromFileCsv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    # Test cases...

if __name__ == "__main__":
    unittest.main()
