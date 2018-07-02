from django.conf.urls import include,url
from . import views

# /graph/
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<notebook_id>[0-9]+)$',views.detail,name = "detail"),
]