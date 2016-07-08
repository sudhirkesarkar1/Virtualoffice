from django.conf.urls import url
from . import views

app_name ='tasks'
urlpatterns = [
	url(r'^$',views.mytasks,name='mytasks'),
    url(r'^create/$', views.createtask, name='taskcreate'),
	url(r'^old/$', views.oldtasks, name='oldtasks'),
	url(r'^completed/$',views.completetask,name='completetask'),
	url(r'^(?P<pk>[0-9]+)/update/$',views.Updatetask.as_view(),name='Updatetask'),
    url(r'^(?P<pk>[0-9]+)/delete/$',views.Deletetask.as_view(),name='Deletetask'),
	url(r'^(?P<pk>[0-9]+)/$',views.Selecttask.as_view(), name='Selecttask'),
	#url(r'^(?P<TO>[-\w]+)/details/$',views.userdetail.as_view(), name='userdetail'),
	
]