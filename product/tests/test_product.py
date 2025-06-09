from django.test import TestCase
from product.serializers.product_serializer import ProductSerializer

class ProductSerializerTest(TestCase):
    def test_product_valid_data(self):
        data = {
            'title': 'Smartphone',
            'description': 'Latest model smartphone.',
            'price': '1999',
            'active': True,
            'category': [
                {
                    'title': 'Electronics',
                    'slug': 'electronics',
                    'description': 'Electronic devices.',
                    'active': True
                }
            ]
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
