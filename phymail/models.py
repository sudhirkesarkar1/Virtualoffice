from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.
		 
class MyMailSendQueryset(models.query.QuerySet):
	def read(self):
		return self.filter(read=True)
		
class MyMailSendManager(models.Manager):
	def get_queryset(self):
		return MyMailSendQueryset(self.model, using=self._db)
		
	def read(self):
		return self.get_queryset().read()
		 

class MyMailSend(models.Model):
	FROM = models.ForeignKey(User,on_delete=models.CASCADE)
	TO_name = models.CharField(max_length=200)
	TO_address_line_1 = models.CharField(max_length=200,null=True,blank=True)
	TO_address_line_2 = models.CharField(max_length=200, null=True,blank=True)
	Town_City = models.CharField(max_length=50,null=True,blank=True)
	State = models.CharField(max_length=50,null=True,blank=True)
	Postcode = models.IntegerField(default=0)
	Your_Message = models.FileField()
	subject = models.CharField(max_length=20,null=True,blank=True)
	slug = models.SlugField(null=True, blank=True)
	read = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)

	objects = MyMailSendManager()
	class Meta:
		ordering = ['-timestamp']
	def __str__(self):
		return self.FROM.username
	def get_absolute_url(self):
		 return reverse('senddetail', kwargs={'slug': self.slug})
		 

	
		 
		 
class MyMailRecieveQueryset(models.query.QuerySet):
	def read(self):
		return self.filter(read=True)
		
class MyMailRecieveManager(models.Manager):
	def get_queryset(self):
		return MyMailRecieveQueryset(self.model, using=self._db)
		
	def read(self):
		return self.get_queryset().read()

class MyMailRecieve(models.Model):
	TO = models.ForeignKey(User,on_delete=models.CASCADE)
	FROM = models.CharField(max_length=200)
	FROM_address = models.TextField()
	Your_Message = models.FileField()
	slug = models.SlugField(null=True, blank=True)
	read = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now= True)

	objects = MyMailRecieveManager()
	class Meta:
		ordering = ['-timestamp']
	def __str__(self):
		return self.FROM
	def get_absolute_url(self):
		 return reverse('recievedetail', kwargs={'slug': self.slug})
		 
		 
		 

def MyMailSend_post_save_receiver(sender, instance, created, *args, **kwargs):
	print("signal sent")
	if created:
		slug_title = slugify(instance.TO_name)
		new_slug = "%s%s" %(instance.TO_name, instance.id)
		try:
			obj_exists = MyMailSend.objects.get(slug=slug_title)
			instance.slug = slugify(new_slug)
			instance.save()
			print("model exists, new slug generated")
		except MyMailSend.DoesNotExist:
			instance.slug = new_slug
			instance.save()
			print("slug and model created")
		except MyMailSend.MultipleObjectsReturned:
			instance.slug = slugify(new_slug)
			instance.save()
			print("multiple models exists, new slug generated")
		except:
			pass



post_save.connect(MyMailSend_post_save_receiver, sender=MyMailSend)


	
