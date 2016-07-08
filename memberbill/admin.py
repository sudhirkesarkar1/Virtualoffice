from django.contrib import admin
from .models import MemberBill,BillHistory

# Register your models here.
class MemberBillAdmin(admin.ModelAdmin):
	list_display = ["__str__","userexpiry","updated"]
	
class BillHistoryAdmin(admin.ModelAdmin):
	list_display = ["__str__","bill_ammount","timestamp"]

admin.site.register(MemberBill,MemberBillAdmin)

admin.site.register(BillHistory,BillHistoryAdmin)