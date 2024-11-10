from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {'fname': "First Name", 'lname': "Last Name", 'phone': "Phone no"}
        widgets = {
            'fname': forms.TextInput(attrs={"class": "form-control"}),
            'lname': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'branch': forms.Select(attrs={"class": "form-control"}),
        }

