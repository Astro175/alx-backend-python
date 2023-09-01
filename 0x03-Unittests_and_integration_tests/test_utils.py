#!/usr/bin/env python3

"""
  Test case for nested maps in utils.py
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
      Test class for nesteed maps
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, output):
        """
          Test method for nested maps
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, output)
    
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         exception):
        """
          Checks for a keyword error
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)



if __name__ == '__main__':
    unittest.main()
