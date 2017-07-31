from django.conf.urls import url

from . import views

app_name = 'properties'


urlpatterns = [
    url(r'^search/$', views.PropertySearchView.as_view(), name='search'),
    url(r'^my-properties/$', views.UserPropertyListView.as_view(), name='my_props'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.PropertyEditView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PropertyDeleteView.as_view(), name='delete'),
    url(r'^create/$', views.PropertyCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.PropertyDetailView.as_view(), name='detail'),
    url(r'^$', views.PropertyListView.as_view(), name='list'),
]
