from django.contrib import admin
from .models import Tasks
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
	list_display = ["__str__","Task_Topic","timestamp"]
	
	
admin.site.register(Tasks,TasksAdmin)
