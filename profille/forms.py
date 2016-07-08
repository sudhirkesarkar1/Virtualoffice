from django import forms
from .models import UserDetail
import re

class UserDetailForm(forms.ModelForm):
	class Meta:
		model=UserDetail
		fields = ['First_name','Last_name','Mobile_number',
					'Address_Line1','Address_Line2','Town_or_City',
					'State','PostCode','Virtual_Office_Location',
					'Active_user'
				]
	def clean_PostCode(self):
		f=self.cleaned_data.get('PostCode')
		if f >100000 and f < 900000:
			return f
		else:
			raise forms.ValidationError(" invalid Postcode")
	def clean_Mobile_number(self):
		f= self.cleaned_data.get('Mobile_number')
		#n = re.findall(r'[7-9][0-9]{9}',f)
		if f >999999999 and f < 10000000000:
			return f
		else :
			raise forms.ValidationError(" enter valid number")
	
	def clean_Active_user(self):
		z= self.cleaned_data.get('Active_user')
		if z == False:
			raise forms.ValidationError(" select field")
		return z

	def clean_First_name(self):
		g=self.cleaned_data.get('First_name')
		if not g:
			raise forms.ValidationError(" valid Album_name")
		if g.isdigit():
			raise forms.ValidationError("Please enter valid Album_name")
		return g
	