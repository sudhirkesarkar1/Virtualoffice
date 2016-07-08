from django.contrib import admin
from .models import UserDetail
from .forms import UserDetailForm

class UserDetailAdmin(admin.ModelAdmin):
	list_display = ["__str__","user","Virtual_Office_Location"]
	#form = UserDetailForm
	fields = ['First_name','Last_name','Mobile_number',
					'Address_Line1','Address_Line2','Town_or_City',
					'State','PostCode','Virtual_Office_Location',
					'Active_user'
				]
	
admin.site.register(UserDetail,UserDetailAdmin)


# Register your models here.
