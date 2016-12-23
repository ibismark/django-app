from django.conf.urls import url
from . import views

app_name = "example"
urlpatterns = [
    url(r'^example/$', views.example, name="example"),
    url(r'^example/test', views.example2, name="example2"),
    #url(r'^(?P<question_id>[0-9]+)/$', views.example2, name='example2'),
]
