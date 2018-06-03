#importing forms
from django import forms 
 
#creating our forms
class SearchForm(forms.Form):
 #django gives a number of predefined fields
 #CharField and EmailField are only two of them
 #go through the official docs for more field details
 query = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search...'}),label='')
 
 page = forms.CharField(widget=forms.HiddenInput(), initial='1')
 