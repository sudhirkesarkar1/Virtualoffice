from django.contrib import admin
from .forms import MeetsForm
from .models import Meets
# Register your models here.

class MeetsAdmin(admin.ModelAdmin):
	list_display = ["__str__","Topic","timestamp"]
	
	
admin.site.register(Meets,MeetsAdmin)