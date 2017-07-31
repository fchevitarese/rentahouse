from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name=_('Full name'), max_length=150)
    phone = models.CharField(verbose_name=_('Phone number'), blank=True,
                             null=True, max_length=11)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __unicode__(self):
        return self.fullname

    def __str__(self):
        return self.fullname

