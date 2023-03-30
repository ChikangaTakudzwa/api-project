from unittest import TestCase
from django.urls import reverse
from . import serializers

class TestSerializer(TestCase):

    def test_category(self):
        """ Test category """
        url = reverse("books")
        resp = client.get(url)
        assert resp.status_code == 200
