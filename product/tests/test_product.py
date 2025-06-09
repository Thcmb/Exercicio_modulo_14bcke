from django.test import TestCase

from product.models import Category
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTest(TestCase):
    def test_product_valid_data(self):
        category = Category.objects.create(
            title='Electronics',
            slug='electronics',
            description='Electronic devices.',
            active=True
        )

        data = {
            'title': 'Smartphone',
            'description': 'Latest model smartphone.',
            'price': 2000,
            'active': True,
            'categories_id': [category.id]  # Campo que o serializer exige
        }

        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        product = serializer.save()
        self.assertEqual(product.title, 'Smartphone')
        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().title, 'Electronics')
