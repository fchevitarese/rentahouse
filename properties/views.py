from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic
from django.views.generic.detail import DetailView
from django.utils.translation import ugettext as _
from django.urls import reverse_lazy

from . import forms, models


class PropertyDetailView(DetailView):
    model = models.Property
    template_name = 'property_detail.html'


class PropertyCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Property
    template_name = 'property_create.html'
    form_class = forms.PropertyCreateForm

    def get_context_data(self, **kwargs):
        context = super(PropertyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = forms.PropertyCreateFormSet(self.request.POST,
                                                             self.request.FILES)
        else:
            context['formset'] = forms.PropertyCreateFormSet()
        return context

    def form_valid(self, form):
        # TODO: Process media. Maybe its on clean method :)
        context = self.get_context_data()
        form = context['form']
        formset = context['formset']

        if form.is_valid() and formset.is_valid():
            form.instance.user = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super(PropertyCreateView, self).form_valid(form)


class PropertyEditView(LoginRequiredMixin, generic.UpdateView):
    model = models.Property
    template_name = 'property_edit.html'
    form_class = forms.PropertyCreateForm
    success_url = '/'

    def get_object(self):
        return models.Property.objects.get(pk=self.kwargs['pk'],
                                           user=self.request.user)


class PropertyListView(generic.ListView):
    model = models.Property
    template_name = 'property_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PropertyListView, self).get_context_data(**kwargs)
        context['header_text'] = _('All properties')
        return context


class UserPropertyListView(PropertyListView):
    def get_queryset(self):
        return models.Property.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(UserPropertyListView, self).get_context_data(**kwargs)
        context['header_text'] = _('My properties')
        return context


class PropertySearchView(PropertyListView):
    def get_context_data(self, **kwargs):
        context = super(PropertySearchView, self).get_context_data(**kwargs)
        context['header_text'] = _('Search result')
        return context

    def get_queryset(self):
        qs = super(PropertySearchView, self).get_queryset()

        search = self.request.GET.get('q')
        if search:
            return qs.filter(Q(street__icontains=search))


class PropertyDeleteView(generic.DeleteView):
    model = models.Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('properties:my_props')
