from django.test import TestCase
from ..models import Country


class CountryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.russia = Country(name='russia')

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.russia, Country))