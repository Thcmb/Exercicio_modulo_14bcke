from django.test import TestCase
from order.factories import ProductFactory, UserFactory  # importe suas factories
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

    def test_order_serializer_read(self):
        # Crie uma order para teste de leitura, se quiser
        pass

    def test_order_serializer_write(self):
        data = {
            "user": self.user.id,
            "products_id": [self.product_1.id, self.product_2.id],
        }
        serializer = OrderSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        order = serializer.save()
        self.assertEqual(order.user.id, self.user.id)
        self.assertEqual(order.product.count(), 2)