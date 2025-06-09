from django.test import TestCase
from django.contrib.auth.models import User

from product.models import Product
from order.serializers.order_serializer import OrderSerializer


class OrderSerializerTest(TestCase):
    def test_order_valid_data(self):
        # Cria usuário
        user = User.objects.create_user(username='testuser', password='123456')

        # Cria produtos
        product1 = Product.objects.create(
            title='Smartphone',
            description='Latest model smartphone.',
            price=2000,
            active=True
        )
        product2 = Product.objects.create(
            title='Laptop',
            description='High-end gaming laptop.',
            price=5000,
            active=True
        )

        # Dados esperados para o serializer
        data = {
            'user': user.id,
            'products_id': [product1.id, product2.id]
        }

        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        order = serializer.save()
        self.assertEqual(order.product.count(), 2)
        self.assertEqual(order.user.username, 'testuser')
