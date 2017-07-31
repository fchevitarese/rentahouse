from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext as _

from . import models


class PropertyCreateForm(forms.ModelForm):
    description = forms.CharField(label=_('Description'),
                                  widget=forms.Textarea)

    class Meta:
        model = models.Property
        fields = ['title', 'description', 'city', 'street', 'complement',
                  'neighborhood', 'state', 'value']
        exclude = ['uuid']


class PropertyPicturesForm(forms.ModelForm):
    class Meta:
        model = models.PropertyPics
        exclude = ['prop', 'url']


PropertyCreateFormSet = inlineformset_factory(models.Property,
                                              models.PropertyPics,
                                              form=PropertyPicturesForm)
