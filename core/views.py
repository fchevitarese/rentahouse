from django.views.generic import TemplateView
from properties.models import Property


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_properties'] = Property.objects.all()
        return context
