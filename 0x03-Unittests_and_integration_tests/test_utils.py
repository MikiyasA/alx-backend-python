#!/usr/bin/env python3
"""
0- Parameterize a unit test, 1- 2- Mock HTTP calls
3- Parameterize and patch
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ Test case """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ To test access_nested_map method outputs """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,  nested_map, path):
        """ to test access_nested_map exceptions """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Test case """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock_get):
        """ to test get_json """
        mock_get.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """ Test case """
    def test_memoize(self):
        """ to test memoize """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
