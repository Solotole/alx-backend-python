#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    "class to carry out unittest"
    @parameterized.expand
    def test_access_nested_map(self):
        "Testing method Access nested map with key path"
        self.assertEqual(access_nested_map({"a": 1}, ["a"]), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ["a"]), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ["a", "b"]), 2)
