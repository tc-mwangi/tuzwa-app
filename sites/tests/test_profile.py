from django.test import TestCase
from ..models import Profile


class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.website = Profile(username='moringa', avatar='', bio='', project='', email='')

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.website, Profile))



