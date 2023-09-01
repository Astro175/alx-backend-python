#!/usr/bin/env python3

"""
  Test case for nested maps in utils.py
"""

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


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

class TestGetJson(unittest.TestCase):
    """
      Test class for json using a mock object and patch
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, output):
        """
           Method that tests get_json
        """
        response_mock = Mock()
        response_mock.json.return_value = output
        with patch('requests.get', return_value=response_mock):
            response = get_json(url)
            self.assertEqual(response, output)


if __name__ == '__main__':
    unittest.main()
