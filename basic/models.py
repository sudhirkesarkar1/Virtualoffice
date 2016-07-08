from django.db import models

class Contact_US(models.Model):
	Name=models.CharField(max_length=50)
	Email=models.EmailField()
	Query=models.TextField()
	Contact_number=models.IntegerField()
	
	def _str_(self):
		return self.Name
# Create your models here.
