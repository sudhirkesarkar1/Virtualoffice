from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from .models import Meets
from profille.models import UserDetail
from .forms import MeetsForm
from datetime import date
import datetime
# Create your views here.


class ProtectedView(generic.TemplateView):
    template_name = 'basee.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)

		
@method_decorator(login_required,name='dispatch')
class userdetail(generic.DetailView):
    model = UserDetail
    template_name = 'userdetail.html'	
	#context_object_name = 'usr'
	#context_object_name = 'usr'

@login_required(login_url='/accounts/login/')
def mymeets(request):
	if request.user.is_superuser:
		aob = Meets.objects.filter(Meeting_Date = datetime.date.today())
		a=[]
		for i in aob:
			a.append(UserDetail.objects.get(user=i.TO))	
		return render(request,'meetings/meetadmin.html',{'aob':aob,'a':a})

	try:
		obj = Meets.objects.filter(TO=request.user,deletee=False)
		abj = UserDetail.objects.get(user=request.user)
		if abj.get_act() == False:
			return HttpResponseRedirect(reverse('memberbill:myaccount'))
		for objj in obj :
			if objj.Meeting_Date < datetime.date.today() :
				objj.deletee = True
				objj.save()
				print(objj.deletee)
		
	except Meets.DoesNotExist:
		obj = None
	except UserDetail.DoesNotExist:
		 return HttpResponseRedirect(reverse('profile'))
	return render(request,'meetings/mymeet.html',{'object':obj})

@login_required(login_url='/accounts/login/')
def oldmeets(request):
	try:
		obj = Meets.objects.filter(TO=request.user,deletee=True)
	except Meets.DoesNotExist:
		obj = None
	return render(request,'meetings/oldmeets.html',{'object':obj})

@login_required(login_url='/accounts/login/')
def createmeet(request):
	try:
		i = Meets.objects.filter(TO=request.user,deletee=False)
		j= i.count()
		if j == 3:
			return render(request,'meetings/mymeet.html',{'data':'you can not add more than 3 meetings sorry','object':i})
	except Meets.DoesNotExist:
		pass
	title= 'Create Meeting'
	form_send = MeetsForm(request.POST or None)
	context={'title':title,'form':form_send}
	if form_send.is_valid():
		instance = form_send.save(commit=False)
		instance.TO = request.user
		dt = instance.Meeting_Date
		try:
			ob =  Meets.objects.filter(Meeting_Date=dt)
			for mt in ob:
				x= mt.Time_From
				y= mt.Time_To
				if x<instance.Time_From<y or x<instance.Time_To<y or x == instance.Time_From or y == instance.Time_To:
					context={'title':title,'data':'select other date or slot time as there is slot for the session %s %s' %(x,y)}
					return render(request,'meetings/createmeet.html',context)
		except:
			pass
		instance.save()
		context={'title':title,'data':'Your Mail has been added'}
	return render(request,'meetings/createmeet.html',context)


@method_decorator(login_required,name='dispatch')
class Updatemeet(generic.UpdateView):
	form_class = MeetsForm
	template_name_suffix='update'
	model = Meets


@method_decorator(login_required,name='dispatch')
class Deletemeet(generic.DeleteView):
	model = Meets
	success_url = reverse_lazy('meetings:mymeetings')


@method_decorator(login_required,name='dispatch')
class Selectmeet(generic.DetailView):
	template_name = 'meetings/meetdetail.html'
	model = Meets
	#context_object_name = 'recieve'
	def get_object(self):
		object = super(Selectmeet, self).get_object()
		#if object.read = True
		#object.save()
		return object
	context_object_name = 'send'
