import factory
from django_factory_boy.auth import UserFactory

from . import models


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Profile
        django_get_or_create = ('fullname', )
    user = factory.SubFactory(UserFactory)
