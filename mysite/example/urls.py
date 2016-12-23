from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^example/$', views.example, name="example"),
    url(r'^example/test', views.example2, name="example2"),
]
