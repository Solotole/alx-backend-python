#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_url, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        mock_response = {"repos_url": "https://api.github.com/orgs/{org}/repos"}
        mock_get_json.return_value = mock_response
        result = client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
