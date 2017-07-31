import factory
from django.test import Client, TestCase
from django.urls import reverse
from django_factory_boy.auth import UserFactory

from . import factories, models


class PropertiesModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = UserFactory(username='test', password='test123')

        self.proper = factories.PropertyFactory(
            user=self.new_user,
            title='MyNewProperty',
            value=100.00
        )

    def test_create_property(self):
        proper = models.Property.objects.create(
            user=self.new_user,
            title='My awesome house for rent',
            description='Rent my house, it\s an amazing house.',
            city='TestCity',
            neighborhood='TestNeighborhood',
            state='MG',
            value=650.00,
        )
        proper.save()
        self.assertEquals(proper.user, self.new_user)
        self.assertEquals(proper.title, 'My awesome house for rent')
        self.assertEquals(proper.value, 650.00)

    def test_property_url_exist(self):
        response = self.client.get(self.proper.get_absolute_url())
        self.assertEquals(response.status_code, 200)


class TestPropertyCreateForm(TestCase):
    def test_property_form_valid(self):
        form = PropertyCreateForm(data={
            'title': 'MyTestProperty',
            'description': 'I have an execelent property to rent for you!',
            'city': 'Rio de Janeiro',
            'neighborhood': 'Copacabana',
            'state': 'RJ',
            'value': 1200.00,
            }
        )
        self.assertTrue(form.is_valid())

    def test_property_form_invalid(self):
        form = PropertyCreateForm(data={
            'title': '',
            'description': '',
            'city': '',
            'neighborhood': '',
            'state': '',
            'value': 0
        })
        self.assertFalse(form.is_valid())
