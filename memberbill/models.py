from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MemberBill(models.Model):
	user =  models.OneToOneField(
			User,
			on_delete=models.CASCADE,
    )
	userexpiry = models.DateField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)
	
	def __str__(self):
		return self.user.username
	
	
class BillHistory(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	bill_ammount=models.IntegerField(default=1000)
    #bill_ammount = models.IntegerField()
	#user = models.ForeignKey(User,on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)
	
	def __str__(self):
		return self.user.username