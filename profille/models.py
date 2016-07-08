from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetail(models.Model):
	user =  models.OneToOneField(
			User,
			on_delete=models.CASCADE,
    )
	First_name = models.CharField(max_length=200)
	Last_name = models.CharField(max_length=200)
	Mobile_number = models.IntegerField(default=0)
	Address_Line1 = models.CharField(max_length=300)
	Address_Line2 = models.CharField(max_length=300)
	Town_or_City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	PostCode = models.IntegerField(default=0)
	Office_CHOICES = (
        ('Andheri', 'Andheri'),
        ('Borivali', 'Borivali'),
        ('Miraroad', 'Miraroad'),
        ('Virar', 'Virar'),
    )
	Virtual_Office_Location = models.CharField(
        max_length=15,
        choices=Office_CHOICES
    )
	Active_user = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)
	def get_act(self):
		return self.Active_user
	
	def __str__(self):
		return self.First_name
