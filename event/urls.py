
from django.conf.urls import url

from event import views

app_name = 'event'

urlpatterns = [

    # /event/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # event/event/entry
    url('entry/$', views.EventEntry.as_view(), name='event-entry'),

    # event/product/2
    url(r'^(?P<pk>[0-9]+)/$', views.EventUpdate.as_view(), name='event-update'),

    # event/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.EventDelete.as_view(), name='event-delete'),

]
