from django import forms
from .models import Contact_US

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact_US
		fields = ['Name','Email','Query','Contact_number']
		
	def clean_Contact_number(self):
		f= self.cleaned_data.get('Contact_number')
		#n = re.findall(r'[7-9][0-9]{9}',f)
		if f >999999999 and f < 10000000000:
			return f
		else :
			raise forms.ValidationError(" enter valid number")
	
	