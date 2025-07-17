
from rest_framework.test import APITestCase
from unittest import TestCase
from restaurant.models import Menu
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse


class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='solomon', password='testpass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu_item = Menu.objects.create(title="Pasta", price=150, inventory=50)

    def test_menu_item_creation(self):
        response = self.client.post('/restaurant/menu/', {'title': 'Pizza', 'price': 200, 'inventory': 30})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(title='Pizza').price, 200)

    def test_menu_item_retrieval(self):
        # response = self.client.get(f'/restaurant/menu/{self.menu_item.id}/')
        response = self.client.get(f'/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(response.data[0]['title'], self.menu_item.title)
        
