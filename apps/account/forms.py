from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=20)
    middle_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(required=False)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    school_college = forms.CharField(max_length=100, required=False)
    major = forms.CharField(max_length=30)
    year_of_study = forms.DateField(required=False)
    graduation_year = forms.DateField(required=False)
    bio = forms.CharField(widget=forms.Textarea(), required=False)