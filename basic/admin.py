from django.contrib import admin
from .models import Contact_US
from .forms import ContactForm

class contactAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	#form = UserDetailForm
	fields = ['Name','Email','Query','Contact_number'
				]
	
admin.site.register(Contact_US,contactAdmin)



# Register your models here.
