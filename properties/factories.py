import factory
from django_factory_boy.auth import UserFactory

from . import models


class PropertyFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Property
        django_get_or_create = ('user', 'title', 'value')
    user = factory.SubFactory(UserFactory)


class PropertyPictureFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.PropertyPics
