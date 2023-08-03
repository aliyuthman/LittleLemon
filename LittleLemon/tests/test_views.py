from django.test import TestCase
from restaurant.models import Menu


# class MenuViewTest(TestCase):
    
 
#     def setUp(self):
#         # Create a few test instances of the Menu model
#         menu1 = Menu.objects.create(title="Menu 1", price=10.99, inventory=5)
#         menu2 = Menu.objects.create(title="Menu 2", price=15.99, inventory=3)
#         menu3 = Menu.objects.create(title="Menu 3", price=8.49, inventory=10)

#     def test_getall(self):
#         url = reverse("menu")  # URL name for listing all menus
#         response = self.client.get(url)

#         # Check if the response status code is 200 OK
#         self.assertEqual(response.status_code, 200)

#         # Serialize the retrieved objects
#         expected_data = [
#             {
#                 "id": menu.id,
#                 "title": menu.title,
#                 "price": str(
#                     menu.price
#                 ), 
#                 "inventory": menu.inventory,
#             }
#             for menu in Menu.objects.all()
#         ]

#         self.assertEqual(response.json(), expected_data)
