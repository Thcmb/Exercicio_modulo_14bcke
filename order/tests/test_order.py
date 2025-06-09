from django.test import TestCase
from order.serializers.order_serializer import OrderSerializer

class OrderSerializerTest(TestCase):
    def test_order_valid_data(self):
        data = {
            'product': [
                {
                    'title': 'Smartphone',
                    'description': 'Latest model smartphone.',
                    'price': 2000,
                    'active': True,
                    'category': [
                        {
                            'title': 'Electronics',
                            'slug': 'electronics',
                            'description': 'Electronic devices.',
                            'active': True
                        }
                    ]
                },
                {
                    'title': 'Laptop',
                    'description': 'High-end gaming laptop.',
                    'price': 5000,
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
            ]
        }
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
