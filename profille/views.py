from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,Http404
from .forms import UserDetailForm
from django.contrib.auth.models import User
from .models import UserDetail
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from memberbill.models import MemberBill,BillHistory
from datetime import date,timedelta
import datetime


@login_required(login_url='/accounts/login/')
def profile(request):
	title = 'Profile'
	#if request.user.is_authenticated():
	if request.user.is_superuser:
		return HttpResponseRedirect(reverse('meetings:mymeetings'))
	try:
		act = UserDetail.objects.get(user=request.user)
		try:
			mbill = MemberBill.objects.get(user=request.user)
			if mbill.userexpiry < datetime.date.today():
				act.Active_user=False
				act.save()
				return HttpResponseRedirect(reverse('memberbill:myaccount'))
		except MemberBill.DoesNotExist:
			pass
		
		
		if act.Active_user == True:
			print('works yeah')
		#return HttpResponseRedirect(reverse('mymail'))
		#return render(request,'basemain.html',{})
			return HttpResponseRedirect(reverse('phymail'))
		else :
			return HttpResponseRedirect(reverse('memberbill:myaccount'))
			
		
	except UserDetail.DoesNotExist:
		if request.method=='POST':
			print(request.POST)
		form_UserDetail = UserDetailForm(request.POST or None)
		context={'title':title,'form':form_UserDetail}
		if form_UserDetail.is_valid():
			inst=form_UserDetail.save(commit=False)
			inst.user = request.user
			inst.save()
			obj = MemberBill(user=request.user,userexpiry = datetime.date.today()+timedelta(days=30))
			obj.save()
			objb = BillHistory(bill_ammount=1000,user=request.user)
			objb.save()
			'''
			obj, created = MemberBill.objects.get_or_create(
				user=request.user,
				userexpiry =datetime.date.today(),
				defaults={'birthday': date(1940, 10, 9)},
				)
			'''
			context={'title':title,'data':'Your data has been added'}
			return HttpResponseRedirect(reverse('phymail'))
		return render(request,'baseprofile.html',context)
	#else:
	#	return render(request,'basee.html',{})
		

# Create your views here.
