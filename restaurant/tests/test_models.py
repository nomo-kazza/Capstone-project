from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_item_creation(self):
        # Test creating a menu item
        item = Menu.objects.create(title="Burger", price=120, inventory=80)
        self.assertEqual(item.title, "Burger")
        self.assertEqual(item.price, 120)
        self.assertEqual(item.inventory, 80)
        self.assertEqual(Menu.objects.count(), 1)

    def test_menu_item_retrieval(self):
        # Test retrieving a menu item
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")

    def test_menu_item_update(self):
        # Test updating a menu item
        item = Menu.objects.create(title="Salad", price=90, inventory=60)
        item.price = 100
        item.save()
        self.assertEqual(Menu.objects.get(title="Salad").price, 100)

    def test_menu_item_deletion(self):
        # Test deleting a menu item
        item = Menu.objects.create(title="Soda", price=50, inventory=200)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)
        self.assertRaises(Menu.DoesNotExist, Menu.objects.get, title="Soda")