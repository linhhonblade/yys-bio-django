from django.test import TestCase

from .models import Shiki


class ShikiModelTests(TestCase):
    def test_create_shiki(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        shiki = Shiki(name='New Shiki', gender='male')
        self.assertEqual(shiki.name, 'New Shiki')
        self.assertEqual(shiki.gender, 'male')
