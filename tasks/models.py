from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

class Tasks(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	End_Date = models.DateField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)
	Task_CHOICES = (
        ('Important', 'Important'),
        ('Normal', 'Normal'),
    )
	Task_Priority = models.CharField(
        max_length=15,
        choices=Task_CHOICES
    )
	Task_Topic = models.CharField(max_length=50)
	Task_Details = models.TextField()
	Task_complete = models.BooleanField(default=False)

	class Meta:
		ordering = ['End_Date']
		
	def __str__(self):
		return self.user.username	
	def get_absolute_url(self):
		 return reverse('tasks:Selecttask', kwargs={'pk': self.id})
