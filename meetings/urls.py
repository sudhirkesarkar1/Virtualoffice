from django.conf.urls import url
from . import views

app_name ='meetings'
urlpatterns = [
	url(r'^$',views.mymeets,name='mymeetings'),
    url(r'^create/$', views.createmeet, name='meetcreate'),
	url(r'^old/$', views.oldmeets, name='oldmeetings'),
	url(r'^(?P<slug>[-\w]+)/update/$',views.Updatemeet.as_view(),name='Updatemeet'),
    url(r'^(?P<slug>[-\w]+)/delete/$',views.Deletemeet.as_view(),name='Deletemeet'),
	url(r'^(?P<slug>[-\w]+)/$',views.Selectmeet.as_view(), name='Selectmeet'),
	#url(r'^(?P<TO>[-\w]+)/details/$',views.userdetail.as_view(), name='userdetail'),
	
]