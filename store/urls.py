from django.conf.urls import url

from . import views #import views so we can use the url


urlpatterns = [
    # url('', views.index), #"/store" will call the method "index" in "views.py"
    url(r'^$', views.listing),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    
]