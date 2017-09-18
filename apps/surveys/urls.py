from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    # url(r'^surveys/new', views.test2),
    url(r'^new$', views.new),
    # url(r'^new$', views.test),
    # url(r'^create$', views.create),
    # url(r'^(?P<number>\d+)$', views.show),
    # url(r'^(?P<number>\d+)/edit$', views.edit2),
    # url(r'^(?P<number>\d+)/delete$', views.destroy),
]
