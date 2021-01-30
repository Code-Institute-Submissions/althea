from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):

    def test_get_home(self):
        """ test index view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class TestAboutViews(TestCase):

    def test_get_about(self):
        """ test about view """
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about_us.html')
