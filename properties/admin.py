from django.contrib import admin
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail

from . import models


class ReadOnlyAdminMixin(object):
    def has_add_permission(self, request):
        return False

    list_display_links = None


@admin.register(models.Property)
class PropertyAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" heigth="150"/>'.format(
            obj.propertypics_set.all()[0].get_image_url())
        )
    image_tag.short_description = 'Image'

    list_display = ('user', 'title', 'city', 'street', 'complement',
                    'neighborhood', 'state', 'value', 'image_tag')
    list_filter = ('neighborhood', 'state', 'user')
    search_fields = ('address', )


@admin.register(models.PropertyPics)
class PropertyPicsAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" heigth="150"/>'.format(
            obj.get_image_url())
        )
    image_tag.short_description = 'Image'

    list_display = ['prop', 'image_tag']
    readonly_fields = ['image_tag']
