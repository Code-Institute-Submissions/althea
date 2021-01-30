from django.test import TestCase
from bag.templatetags.bag_tools import calc_subtotal
from django.urls import reverse


# tools test
class TestBagTools(TestCase):
    """ test bag subtotal """
    def test_calc_subtotal(self):
        result = calc_subtotal(3, 6)
        self.assertEqual(18, result)


# view tests
class TestBagViews(TestCase):
    def test_get_bag(self):
        """ test bag view """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
