from django.conf.urls import include,url
from . import views


# /graph/
urlpatterns = [
    url(r'^$',views.index,name='index'),
]