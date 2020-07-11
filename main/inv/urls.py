from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path("", views.index, name='inv'),
    url(r'^ce/$', views.computer_entry, name='ce'),
    url(r'^cl/$', views.computer_list, name='cl'),
    url(r'^search/$', views.search, name='search'),
    url(r'^cl/(?P<id>\d+)/delete$', views.computer_delete, name='computer_delete'),
    url(r'^cl/(?P<id>\d+)/$', views.computer_edit, name='computer_edit'),
    url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
