from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from .models import Tasks
from profille.models import UserDetail
from .forms import TasksForm,TaskuForm
from datetime import date
import datetime


# Create your views here.
class ProtectedView(generic.TemplateView):
    template_name = 'basee.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


@login_required(login_url='/accounts/login/')
def mytasks(request):
	context={}
	try:
		abj = UserDetail.objects.get(user=request.user)
		if abj.get_act() == False:
			return HttpResponseRedirect(reverse('memberbill:myaccount'))
		obj = Tasks.objects.filter(user=request.user)
		aaj_i =[]
		aaj_n=[]
		fu_i=[]
		fu_n=[]
		for objj in obj :
			if objj.End_Date == datetime.date.today() and objj.Task_Priority=='Important':
				aaj_i.append(objj)
			if objj.End_Date == datetime.date.today() and objj.Task_Priority=='Normal':
				aaj_n.append(objj)
			if objj.End_Date > datetime.date.today() and objj.Task_Priority=='Important':
				fu_i.append(objj)
			if objj.End_Date > datetime.date.today() and objj.Task_Priority=='Normal' :
				fu_n.append(objj)
		if aaj_i:
			context['aaj_i']=aaj_i
		if aaj_n:
			context['aaj_n']=aaj_n
		if fu_i:
			context['fu_i']=fu_i
		if fu_n:
			context['fu_n']=fu_n
		if not aaj_i and not aaj_n and not fu_i and not fu_n:
			context['tas']='no future or current tasks'
	except Tasks.DoesNotExist:
		obj = None
		context['data']='no tasks'
	except UserDetail.DoesNotExist:
		 return HttpResponseRedirect(reverse('profile'))
	return render(request,'tasks/mytasks.html',context)



@login_required(login_url='/accounts/login/')
def createtask(request):
	title= 'Create Tasks'
	form_send = TasksForm(request.POST or None)
	context={'title':title,'form':form_send}
	if form_send.is_valid():
		instance = form_send.save(commit=False)
		instance.user = request.user
		instance.save()
		context={'title':title,'data':'Your task has been added'}
	return render(request,'tasks/createtask.html',context)

	
@login_required(login_url='/accounts/login/')
def oldtasks(request):
	context={}
	try:
		obj = Tasks.objects.filter(user=request.user)
		old_i =[]
		old_n=[]
		context={}
		for objj in obj :
			if objj.End_Date < datetime.date.today() and objj.Task_Priority=='Important' and objj.Task_complete==False:
				old_i.append(objj)
			if objj.End_Date < datetime.date.today() and objj.Task_Priority=='Normal' and objj.Task_complete==False :
				old_n.append(objj)
			'''
			if objj.End_Date > datetime.date.today() and objj.Task_Priority='Important' :
				fu_i.append(objj)
			if objj.End_Date > datetime.date.today() and objj.Task_Priority='Normal' :
				fu_n.append(objj)
			'''
		if old_i:
			context['old_i']=old_i
		if old_n:
			context['old_n']=old_n
		'''
		if fu_i:
			context['fu_i']=fu_i
		if fu_n:
			context['fu_i']=fu_n
		'''	
	except Tasks.DoesNotExist:
		obj = None
		context['data']='no tasks'
	return render(request,'tasks/oldtasks.html',context)


@login_required(login_url='/accounts/login/')
def completetask(request):
	context={}
	try:
		obj = Tasks.objects.filter(user=request.user)
		old_i =[]
		old_n=[]
		context={}
		for objj in obj :
			if objj.End_Date < datetime.date.today() and objj.Task_Priority=='Important' and objj.Task_complete==True :
				old_i.append(objj)
			if objj.End_Date < datetime.date.today() and objj.Task_Priority=='Normal' and objj.Task_complete==True:
				old_n.append(objj)
			'''
			if objj.End_Date > datetime.date.today() and objj.Task_Priority='Important' :
				fu_i.append(objj)
			if objj.End_Date > datetime.date.today() and objj.Task_Priority='Normal' :
				fu_n.append(objj)
			'''
		if old_i:
			context['old_i']=old_i
		if old_n:
			context['old_n']=old_n
		if not old_i and not old_n:
			context['tas']='no old complete tasks'
		'''
		if fu_i:
			context['fu_i']=fu_i
		if fu_n:
			context['fu_i']=fu_n
		'''	
	except Tasks.DoesNotExist:
		obj = None
		context['data']='no tasks'
	return render(request,'tasks/completetasks.html',context)


@method_decorator(login_required,name='dispatch')
class Updatetask(generic.UpdateView):
	form_class = TaskuForm
	template_name_suffix='update'
	model = Tasks


@method_decorator(login_required,name='dispatch')
class Deletetask(generic.DeleteView):
	model = Tasks
	success_url = reverse_lazy('tasks:mytasks')


@method_decorator(login_required,name='dispatch')
class Selecttask(generic.DetailView):
	template_name = 'tasks/tasksdetail.html'
	model = Tasks
	#context_object_name = 'recieve'
	def get_object(self):
		object = super(Selecttask, self).get_object()
		#if object.read = True
		#object.save()
		return object
	context_object_name = 'send'
