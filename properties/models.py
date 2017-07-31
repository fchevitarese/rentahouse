import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from . import choices


class Property(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(_('Short title'), max_length=50)
    description = models.TextField(_('Description'))
    city = models.CharField(_('City'), max_length=50)
    street = models.CharField(_('Street'), max_length=100, blank=True,
                              null=True)
    complement = models.CharField(_('Complement'), max_length=100, blank=True,
                                  null=True)
    neighborhood = models.CharField(_('Neighborhood'), max_length=50)
    state = models.CharField(_('State'), max_length=2, choices=choices.STATE_CHOICES)
    value = models.DecimalField(_('Rent value'), decimal_places=2, max_digits=6)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True, )

    class Meta:
        """Meta definition for Property."""
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return absolute url for Property."""
        return reverse('properties:detail', kwargs={'pk': self.pk})


class PropertyPics(models.Model):
    # TODO: Override save and send to s3.
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    picture = models.FileField(_('Picture'), upload_to='media/properties',
                               null=True, blank=True)
    thumbnail = ImageSpecField(source='picture',
                               processors=[ResizeToFill(150, 150)],
                               format='JPEG',
                               options={'quality': 60})
    url = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        """Meta definition for PropertyPics."""
        verbose_name = 'Property Picture'
        verbose_name_plural = 'Property Pictures'

    def __unicode__(self):
        return self.picture

    def get_image_url(self):
        return '{static}{file}'.format(
            static=settings.STATIC_URL,
            file=self.picture
        )
