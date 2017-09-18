from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.display),     # This line has changed!
    # url(r'^surveys/new', views.test2),
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^new', views.new),
    # url(r'^surveys/', include('apps.surveys.urls')),
    # url(r'^(?P<number>\d+)$', views.show),
    # url(r'^(?P<number>\d+)/edit$', views.edit2),
    # url(r'^(?P<number>\d+)/delete$', views.destroy),
]
