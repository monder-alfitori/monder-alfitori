from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    content = forms.CharField(widget=forms.Textarea)


class CareerForm(forms.Form):
    fname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter Your First Name'}))
    lname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Last Name'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Age'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}))
    content = forms.CharField(widget=forms.Textarea)