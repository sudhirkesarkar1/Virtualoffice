from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse,Http404
from .models import Contact_US
from .forms import ContactForm
# Create your views here.

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_logout'))
	if request.method == 'POST':
		print(request.POST)
	form=ContactForm(request.POST or None)
	context = {"form":form}
	
	if form.is_valid():
		instance= form.save(commit=False)
		
		instance.save()
		context={ "query":"your Query is submitted"}
		return render(request,"basee.html",context)
	return render(request,'basee.html',context)
	
def trying(request):
	return render(request,'basic/try.html',{})

def	mysite(request):
	return render(request,'basic/mail.html',{})
	
#def contact(request):
	