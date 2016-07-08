from django.shortcuts import render
from .models import MemberBill,BillHistory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from profille.models import UserDetail
from datetime import date,timedelta
import datetime

# Create your views here.


@login_required(login_url='/accounts/login/')
def myaccount(request):
	if request.user.is_superuser:
		try:
			mb = MemberBill.objects.filter(userexpiry < datetime.date.today())
			return render(request,'memberbill/inactiveuser.html',{'mb':mb})
		except:
			return render(request,'memberbill/inactiveuser.html',{})
		
	obj = MemberBill.objects.get(user = request.user)
	
	if obj.userexpiry > datetime.date.today():
		context={'object':obj}
		return render(request,'memberbill/information.html',context)
	else:
		context={'obj':obj,'data':'please pay the bill'}
		return render(request,'memberbill/information.html',context)
	#except:
	#	return HttpResponseRedirect(reverse('profile'))
	
@login_required(login_url='/accounts/login/')	
def billhistory(request):
	obj = MemberBill.objects.get(user = request.user)
	if obj.userexpiry < datetime.date.today():
		objb = BillHistory(bill_ammount=1000,user=request.user)
		objb.save()
		obj.userexpiry = datetime.date.today()+timedelta(days=30)
		obj.save()
		act = UserDetail.objects.get(user=request.user)
		act.Active_user=True
		act.save()
		objectt= BillHistory.objects.filter(user=request.user)
		context ={'objectt':objectt,'data':'Your payment is done','obj':obj}
		return render(request,'memberbill/billhistory.html',context)
	else:
		objectt= BillHistory.objects.filter(user=request.user)
		context={'objectt':objectt}
		return render(request,'memberbill/billhistory.html',context)
		