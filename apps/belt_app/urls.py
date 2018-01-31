from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^user$', views.index),
    url(r'^home$', views.login),
    url(r'^add$', views.add),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^homepage$', views.homepage),
    url(r'^poke/(?P<id>\d+)', views.poke),
]