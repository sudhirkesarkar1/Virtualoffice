from django.conf.urls import url
from . import views

app_name ='memberbill'

urlpatterns = [
	url(r'^$',views.myaccount,name='myaccount'),
	url(r'^billhistory/$',views.billhistory,name='billhistory'),
]