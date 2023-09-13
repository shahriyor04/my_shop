# from django.test import TestCase
# from .models import Client
#
#
# class ClientModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create test data for the model
#         Client.objects.create(username='ali', phone='992446022')
#
#     def test_name_field(self):
#         client = Client.objects.get(id=1)
#         field_label = client._meta.get_field('username').verbose_name
#         self.assertEqual(field_label, 'username')
#
#     def test_phone_field(self):
#         client = Client.objects.get(id=1)
#         field_label = client._meta.get_field('phone').verbose_name
#         self.assertEqual(field_label, 'phone')
#
#     def test_phone_unique_constraint(self):
#         # Attempt to create a client with a duplicate email, should raise IntegrityError
#         with self.assertRaises(Exception):
#             Client.objects.create(username='ali ', phone='992446022')
#
#     def test_string_representation(self):
#         client = Client.objects.get(id=1)
#         self.assertEqual(str(client), 'Test Client')
