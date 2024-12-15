from django import forms

class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message =forms.CharField(required=False,widget=forms.Textarea)
    image = forms.ImageField()\
    

class Email_sender(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)
    to_email = forms.EmailField(required=True)


    
    