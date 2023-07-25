from django.test import TestCase
from inventory.models import Ingredient


class PostTestCase(TestCase):
    def testPost(self):
        post = Ingredient(name="Apple", unit="pound", unit_price=3)
        self.assertEqual(post.name, "Apple")
        self.assertEqual(post.unit, "pound")
        self.assertEqual(post.unit_price, 3)