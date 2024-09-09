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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test that public_repos returns the correct list based on mocked data"""
        mock_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}},
            {"name": "repo3", "license": {"key": "MIT"}},
        ]
        mock_repos_url = "https://api.github.com/orgs/test_org/repos"
        with patch('client.GithubOrgClient._public_repos_url', mock_repos_url):
            # Set the return value of the mocked get_json
            mock_get_json.return_value = mock_payload
            # Instantiate the GithubOrgClient
            client = GithubOrgClient("test_org")
            # Call public_repos without filtering
            result = client.public_repos()
            # Verify the result
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            # Verify that get_json was called once with the mock_repos_url
            mock_get_json.assert_called_once_with(mock_repos_url)


if __name__ == "__main__":
    unittest.main()
