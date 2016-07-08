from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

class MeetsQueryset(models.query.QuerySet):
	def delete(self):
		return self.filter(delete=True)
		
class MeetsManager(models.Manager):
	def get_queryset(self):
		return MeetsQueryset(self.model, using=self._db)
		
	def delete(self):
		return self.get_queryset().delete()

class Meets(models.Model):
	TO = models.ForeignKey(User,on_delete=models.CASCADE)
	Topic = models.CharField(max_length=50)
	slug = models.SlugField(null=True, blank=True)
	deletee = models.BooleanField(default=False)
	Time_From = models.IntegerField()
	Time_To = models.IntegerField()
	Meeting_Date = models.DateField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)
	
	objects = MeetsManager()
	class Meta:
		ordering = ['-Meeting_Date']
		unique_together = ('Time_From', 'Meeting_Date','Time_To')
	def __str__(self):
		return self.TO.username
	def get_absolute_url(self):
		 return reverse('Selectmeet', kwargs={'slug': self.slug})
	
	

def Meets_post_save_receiver(sender, instance, created, *args, **kwargs):
	print("signal sent")
	if created:
		slug_title = slugify(instance.Topic)
		new_slug = "%s%s" %(instance.Topic.replace(" ", ""),instance.id)
		try:
			obj_exists = Meets.objects.get(slug=slug_title)
			instance.slug = slugify(new_slug)
			instance.save()
			print("model exists, new slug generated")
		except Meets.DoesNotExist:
			instance.slug = new_slug
			instance.save()
			print("slug and model created")
		except Meets.MultipleObjectsReturned:
			instance.slug = slugify(new_slug)
			instance.save()
			print("multiple models exists, new slug generated")
		except:
			pass


post_save.connect(Meets_post_save_receiver, sender=Meets)
