from django import forms
#import floppyforms as forms
from .models import Meets
import datetime

class DateInput(forms.DateInput):
	#template_name = 'datepicker.html'
    input_type = 'date'
	
	
class MeetsForm(forms.ModelForm):
	class Meta:
		model=Meets
		fields = ['Topic','Time_From','Time_To','Meeting_Date']
		widgets = {
            'Meeting_Date': DateInput(),
        }
		
	def clean_Topic(self):
		g=self.cleaned_data.get('Topic')
		if not g:
			raise forms.ValidationError("not valid TOpic")
		if g.isdigit():
			raise forms.ValidationError("Please enter valid TOpic")
		return g
		
	def clean_Time_From(self):
		g=self.cleaned_data.get('Time_From')
		if 9 > g or g >= 17:
			raise forms.ValidationError(" Time should be between 9-17 follow 24 hrs clocksystem ")
		return g
		
	def clean_Time_To(self):
		g = self.cleaned_data.get('Time_To')
		#d = self.cleaned_data['Meeting_Date']
		#try :
		#	obj = Meets.objects.filter(Meeting_Date = d)
		#	for i in obj:
		#		x= i.Time_From
		#		y= i.Time_To
		#		if x<g<y:
		#			raise forms.ValidationError("select other date or slot time as there is slot for the session %s %s" %(x,y))
		#except Meets.DoesNotExist:
		#	pass
			
		if g <= self.cleaned_data.get('Time_From'):
			raise forms.ValidationError(" really -_- -_- ")
		#if g > self.cleaned_data.get('Time_From'):
		#	raise forms.ValidationError(" select proper end time for your meeting ")
		if 10 > g or g > 17:
			raise forms.ValidationError("Time should be between 9-17 follow 24 hrs clocksystem")
		return g
		
	def clean_Meeting_Date(self):
		g = self.cleaned_data['Meeting_Date']
		if g <= datetime.date.today():
			raise forms.ValidationError("for meetings you can not select today or older dates ")
		return g
	'''	
	def clean(self):
		g = self.cleaned_data.get('Time_To')
		d = self.cleaned_data['Meeting_Date']
		try :
			obj = Meets.objects.filter(Meeting_Date = d)
			for i in obj:
				x= i.Time_From
				y= i.Time_To
				if x<g<y:
					raise forms.ValidationError("select other date or slot time as there is slot for the session %s %s" %(x,y))
		except Meets.DoesNotExist:
			return g
	'''	
		
		
	'''	
	def Your_Message(self):
		f= self.cleaned_data.get('Your_Message')
		if not f:
			raise forms.ValidationError(" select your mail massege")
		if not f.name.endswith('.pdf'):
			raise forms.ValidationError(" please select pdf file ")
		return f
	'''		