#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Class to carry out unittest for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing method access_nested_map with key path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """assertRaises context manager to test that a KeyError
        is raised for the following inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected result and mocks requests.get"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""
    def test_memoize(self):
        """Test that a_property is memoized and a_method is only called once"""
        class TestClass:
            """Class to test memoization"""
            def a_method(self):
                """first method"""
                return 42

            @memoize
            def a_property(self):
                """second method"""
                return self.a_method()
        test_instance = TestClass()
        with patch.object(
                        TestClass, 'a_method', return_value=42
                        ) as mock_method:
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property
            mock_method.assert_called_once()
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)


if __name__ == "__main__":
    unittest.main()
