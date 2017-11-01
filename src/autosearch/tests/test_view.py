from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status


class ViewTestCase(TestCase):
    """test suite for the APIview
    """

    def setup(self):
        """Define the test client and other test variable
        """
        self.client = APIClient()

    def test_view_edcs(self):
        response = self.client.get('/autosearch/edcs')
        self.assertEqual(response.status_code, 200)

    def test_view_edch(self):
        response = self.client.get('/autosearch/edch')
        self.assertEqual(response.status_code, 200)

    def test_view_tegs(self):
        response = self.client.get('/autosearch/tegs')
        self.assertEqual(response.status_code, 200)

    def test_view_tegh(self):
        response = self.client.get('/autosearch/tegh')
        self.assertEqual(response.status_code, 200)
