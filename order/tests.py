from django.urls import reverse
from django.test import tag

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Order, Pizza, Customer


class OrderTests(APITestCase):
    """Test for API endpoints"""

    # load pre-defined fixtures
    fixtures = ['pizza_fixtures.json']

    def setUp(self):
        Order.objects.create(pizza_id=Pizza.objects.get_or_create(name="Hawaii")[0],
                             pizza_size=50,
                             customer_name=Customer.objects.get_or_create(full_name="Max M.")[0],
                             customer_address="Test Avenue 12")

    @tag('post')
    def test_create_order(self):
        """test for PUSH request to orders-list."""
        url = reverse('orders-list')
        data = {
            'pizza_id': 2,
            'pizza_size': 30,
            'customer_name': "John Doe",
            'customer_address': "Test Str. 22"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.all().count(), 2)
        self.assertEqual(Order.objects.get(pk=2).customer_name.full_name, "John Doe")

    @tag('get')
    def test_retrieve_orders(self):
        """test for GET request to orders-list."""
        url = reverse('orders-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Order.objects.all().count())

    @tag('put')
    def test_update_order(self):
        """test for PUT request to orders-detail."""
        url = reverse('orders-detail', kwargs={'pk': Order.objects.all()[0].pk, })
        data_1 = {
            'pizza_id': Pizza.objects.get(name='Napolitana').pk,
            'pizza_size': 50,
            'customer_name': "James Dean",
            'customer_address': "New Avenue 2a",
        }
        response_1 = self.client.put(url, data_1, format='json')
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertTrue(Order.objects.get(customer_address=response_1.data["customer_address"],
                                          customer_name__full_name=response_1.data["customer_name"],
                                          pizza_id=Pizza.objects.get(name='Napolitana').pk,
                                          pizza_size=50))

        data_2 = {
            'pizza_id': data_1["pizza_id"],
            'pizza_size': 50,
            'customer_address': "Test Str. 12a"
        }
        response_2 = self.client.put(url, data_2, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.data.get("customer_name"), "James Dean")
        self.assertEqual(response_2.data.get("customer_address"), "Test Str. 12a")
