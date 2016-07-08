from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.phymail,name='phymail'),
    url(r'^create/$', views.createmailview, name='create'),
	url(r'^send/$',views.sendmail,name='sendmail'),
    url(r'^old/$',views.oldmail,name='oldmail'),
	url(r'^(?P<slug>[-\w]+)/$',views.RecieveView.as_view(), name='recievedetail'),
	
	url(r'^send/(?P<slug>[\w-]+)/$',views.SendView.as_view(),name='senddetail')
	
]