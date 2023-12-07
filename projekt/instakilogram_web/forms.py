from django import forms
from .models import Insta_users

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Hasło', widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'input'}))
    class Meta:
        model = Insta_users
        fields = ["username", "email", "password"]

class EditForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    imgThumb = forms.ImageField(required=False, widget=forms.FileInput)
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'textarea'}))
    gender = forms.ChoiceField(required=False,widget=forms.Select(attrs={'class': 'select'}),
    choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    class Meta:
        model = Insta_users
        fields = ["email", "password", "imgThumb", "last_name", "first_name","description", "gender",]

class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(label='Hasło', widget=forms.TextInput(attrs={'class': 'input'}))