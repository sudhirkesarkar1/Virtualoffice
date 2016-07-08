from django import forms
from .models import MyMailSend,MyMailRecieve

class MyMailSendForm(forms.ModelForm):
	class Meta:
		model=MyMailSend
		fields = ['TO_name','TO_address_line_1','TO_address_line_2','Town_City','State','Postcode','Your_Message']
		
	def TO_name(self):
		g=self.cleaned_data.get('TO_name')
		if not g:
			raise forms.ValidationError("not valid TO_name")
		if g.isdigit():
			raise forms.ValidationError("Please enter valid TO_name")
		return g
		
	def clean_Your_Message(self):
		f= self.cleaned_data.get('Your_Message')
		if not f:
			raise forms.ValidationError(" select your mail massege")
		if not f.name.endswith('.pdf'):
			raise forms.ValidationError(" please select pdf file ")
		return f
		