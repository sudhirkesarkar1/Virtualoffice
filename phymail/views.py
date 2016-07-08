from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import MyMailSend,MyMailRecieve
from .forms import MyMailSendForm
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from profille.models import UserDetail

# Create your views here.




class ProtectedView(generic.TemplateView):
    template_name = 'basee.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


@login_required(login_url='/accounts/login/')
def phymail(request):
	try:
		obj = MyMailRecieve.objects.filter(TO=request.user,read=False)
		#print(obj)
		abj = UserDetail.objects.get(user=request.user)
		if abj.get_act() == False:
			return HttpResponseRedirect(reverse('memberbill:myaccount'))
	except MyMailRecieve.DoesNotExist:
		obj = None
	except UserDetail.DoesNotExist:
		 return HttpResponseRedirect(reverse('profile'))
	return render(request,'phymail/mymail.html',{'object':obj})
	
@login_required(login_url='/accounts/login/')
def oldmail(request):
	try:
		obj = MyMailRecieve.objects.filter(TO=request.user).read()
		print(obj)
	except MyMailRecieve.DoesNotExist:
		obj = None
	return render(request,'phymail/oldmail.html',{'object':obj})
		
	
	
	
@login_required(login_url='/accounts/login/')
def createmailview(request):
	title= 'Create mail'
	form_send = MyMailSendForm(request.POST or None, request.FILES or None)
	context={'title':title,'form':form_send}
	if form_send.is_valid():
		instance = form_send.save(commit=False)
		instance.FROM = request.user
		instance.save()
		context={'title':title,'data':'Your Mail has been added'}
	return render(request,'phymail/createmail.html',context)
		

#@login_required(login_url='/accounts/login/')
@method_decorator(login_required,name='dispatch')
class RecieveView(generic.DetailView):
	template_name = 'phymail/recievedetail.html'
	model = MyMailRecieve
	context_object_name = 'recieve'
	def get_object(self):
		object = super(RecieveView, self).get_object()
		object.read = True
		object.save()
		return object
	context_object_name = 'recieve'
		
		
@login_required(login_url='/accounts/login/')
def sendmail(request):
	try:
		obj = MyMailSend.objects.filter(FROM=request.user)
		print(obj)
	except MyMailSend.DoesNotExist:
		obj=None
	return render(request,'phymail/sentmail.html',{'obj':obj})

#@login_required(login_url='/accounts/login/')
@method_decorator(login_required,name='dispatch')
class SendView(generic.DetailView):
	template_name = 'phymail/senddetail.html'
	model = MyMailSend
	context_object_name = 'send'
	