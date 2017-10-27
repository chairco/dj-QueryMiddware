from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .views import EdcGlasscHistoryViewSet


class ViewSetTest(TestCase):
    """test suite for the api viewset
    """

    def test_view_set(self):
        requests = APIRequestFactory().get("")
        edc_detail = EdcGlasscHistoryViewSet.as_view({'get': 'list'})
        response = edc_detail(requests)
        self.assertEqual(response.status_code, 200)


class ViewTestCase(TestCase):
    """test suite for the api view
    """

    def setup(self):
        """Define the test client and other test variable
        """
        self.client = APIClient()
        self.glassid = {'glassid': 'TL6AS0KAF'}
        self.response = self.client.get()
