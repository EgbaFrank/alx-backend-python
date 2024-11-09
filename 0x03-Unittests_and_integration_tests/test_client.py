#!/usr/bin/env python3
"""
Client test module
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Contains test cases for the github_org_client class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """test case for the org property
        """
        expected_response = {"login": org, "id": 12345, "type": "Organization"}
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org)
        result = client.org

        url = f'https://api.github.com/orgs/{org}'

        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, expected_response)

    def test_public_repos_url(self):
        """Test cases for the public_repos_url method
        """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_repo:
            url = "https://api.github.com/orgs/example_org/repos"
            mock_repo.return_value = {"repos_url": url}
            client = GithubOrgClient("example_org")
            self.assertEqual(client._public_repos_url, url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test cases for the public repo method
        """
        expected_response = [
            {'name': 'test'},
            {'name': 'repo'},
            {'name': 'check'}
        ]
        mock_get_json.return_value = expected_response

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repo_url:
            url = "https://api.github.com/orgs/org/repos"
            mock_repo_url.return_value = url
            client = GithubOrgClient("org")
            self.assertEqual(client.public_repos(), ['test', 'repo', 'check'])

            mock_repo_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, status):
        """test cases for the has_license method
        """
        client = GithubOrgClient("example_org")
        self.assertEqual(client.has_license(repo, license_key), status)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class-wide mocks for external requests"""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def get_json_side_effect(url, *args, **kwargs):
            """Check the URL and return the corresponding fixture
            """
            if url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            elif url == "https://api.github.com/orgs/google":
                return cls.org_payload
            return []

        mock_get.side_effect = (
            lambda url: Mock(
                json=lambda: get_json_side_effect(url)
            )
        )

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for the public_repos method
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for the public_repos method with license
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
