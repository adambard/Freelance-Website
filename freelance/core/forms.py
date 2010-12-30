from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	description = forms.CharField(required=True, min_length=10, widget=forms.Textarea)
