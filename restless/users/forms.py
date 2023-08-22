from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterFrom(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class' : 'w-full mt-2 mb-2 h-10 py-2 resize-none px-6 bg-white rounded-xl text-black', 'placeholder':'johndoe'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'w-full mt-2 mb-2 py-2 px-6 bg-white rounded-xl text-black', 'placeholder':'johndoe@email.com'}))
    first_name = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class' : 'w-full mt-2 mb-2 h-10 py-2 resize-none px-6 bg-white rounded-xl text-black', 'placeholder':'John'}))
    last_name = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class' : 'w-full mt-2 mb-2 h-10 py-2 resize-none px-6 bg-white rounded-xl text-black', 'placeholder':'Doe'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class' : 'w-full mt-2 mb-2 h-10 py-2 px-6 bg-white rounded-xl text-black'}), label='Password')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class' : 'w-full mt-2 mb-2 h-10 py-2 px-6 bg-white rounded-xl text-black'}), label='Repeat Password')

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class' : 'w-full mt-2 mb-2 py-2 px-6 bg-white rounded-xl text-black'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'w-full mt-2 mb-2 py-2 px-6 bg-white rounded-xl text-black'}))

    