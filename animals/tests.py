from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from animals.models import Animal, User
from django.core import serializers
import json

class AnimalsTests(APITestCase):
  def setUp(self):
    user = User.objects.create_user(username='user', email='user@example.com', password='top_secret')
    self.animal = Animal.objects.create(user_id=user.id, name='tier', physical_description='some description')
    url = reverse('animal-list')
    self.response = self.client.get(url, format='json')
    self.responseList = json.loads(self.response.content)
    self.responseItems = self.responseList[0]

  def test_index_status(self):
    self.assertEqual(self.response.status_code, status.HTTP_200_OK)

  def test_index_count(self):
    self.assertEqual(len(self.responseList), 1)

  def test_index_content_specie_id(self):
    self.assertEqual(self.responseItems['specie_id'], self.animal.specie_id)

  def test_index_content_user_id(self):
    self.assertEqual(self.responseItems['user_id'], self.animal.user_id)

  def test_index_content_name(self):
    self.assertEqual(self.responseItems['name'], self.animal.name)

  def test_index_content_physical_description(self):
    self.assertEqual(self.responseItems['physical_description'], self.animal.physical_description)
