from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mysite/$',views.mysite,name='mysite'),
	url(r'^$',views.index,name = 'index'),
	url(r'^trying/$',views.trying,name='trying'),

]