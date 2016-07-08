from django.contrib import admin
from .forms import MyMailSendForm
from .models import MyMailSend,MyMailRecieve

class MyMailSendAdmin(admin.ModelAdmin):
	list_display = ["__str__","TO_name","timestamp"]
	
class MyMailRecieveAdmin(admin.ModelAdmin):
	list_display = ["__str__","FROM","timestamp"]
	
	
admin.site.register(MyMailRecieve,MyMailRecieveAdmin)
admin.site.register(MyMailSend,MyMailSendAdmin)

# Register your models here.
