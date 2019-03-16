from django.test import TestCase
from ..models import Category


class CategoryTestClass(TestCase):
    #set up method
    def setUp(self):
        self.website = Category(name='website')

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.website, Category))



    

