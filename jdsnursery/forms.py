from django import forms

class ContactForm(forms.Form):
  Full_Name = forms.CharField(label="Full_Name",max_length=300)
  Email = forms.EmailField()
  Phone_no = forms.CharField(max_length=100)
  Message = forms.CharField(widget=forms.Textarea)