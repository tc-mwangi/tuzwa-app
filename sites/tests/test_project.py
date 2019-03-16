from django.test import TestCase
from ..models import Project


class ProjectTestClass(TestCase):
    #set up method
    def setUp(self):
        self.Mogney = Project(
            username='Red Collar',
            avatar='media/screenshot/20190314162341_BIvBeAT.jpg',
            title='Mogney',
            screenshot='',
            description='A new generation of payments. All you need is a QR code.',
            link='https://mogney.com/',
            published_date='2019-02-17',
            category='app',
            country='Russia'
            )

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Mogney, Project))


 