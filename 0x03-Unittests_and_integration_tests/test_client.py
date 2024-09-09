#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient



class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""
    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc"),
    ])
    @patch('client.get_json')
    def test_org(
        self,
        org_name: str,
        expected_url: str,
        mock_get_json: MagicMock
    ) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        mock_response = {
            "repos_url": "https://api.github.com/orgs/{org}/repos"
            }
        mock_get_json.return_value = mock_response
        result = client.org
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_response)

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org: MagicMock) -> None:
        """Test that _public_repos_url returns the correct value based on the mocked org"""
        mock_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        mock_org.return_value = mock_payload
        client = GithubOrgClient("test_org")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
