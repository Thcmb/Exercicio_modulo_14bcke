from django.test import TestCase
from product.serializers.category_serializer import CategorySerializer

class CategorySerializerTest(TestCase):
    def test_category_valid_data(self):
        data = {
            'title': 'Books',
            'slug': 'books',
            'description': 'A collection of books.',
            'active': True,
        }
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
