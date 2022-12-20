from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=100)
    most_recent_employer = forms.CharField(max_length=100)
    employer_2 = forms.CharField(max_length=100)
    employer_3 = forms.CharField(max_length=100)
    school = forms.CharField(max_length=100)
    skills = forms.CharField(max_length=500)
