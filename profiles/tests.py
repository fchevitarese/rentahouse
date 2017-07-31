from django.test import TestCase
import factory
from django_factory_boy.auth import UserFactory

from . import models
from . import factories


class ProfileModelTest(TestCase):
    def test_create_profile(self):
        profile = factories.ProfileFactory(fullname='Name and surname',
                                           phone='31111111111')
        self.assertEqual(profile.fullname, 'Name and surname')
        self.assertEqual(profile.phone, '31111111111')
        self.assertEqual(1, models.Profile.objects.count())
