from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Guardians, Children
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField

# from .models import Articles

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2', ]


class GuardiansForm(forms.ModelForm):
    class Meta:
        model=Guardians
        fields=["name", "phoneNumber", "email", "idNumber", "location", "dp"]


class ChildrensForm(forms.ModelForm):
    class Meta:
        model=Children
        fields=["name", "birth_cert_number", "birth_cert", "passport"]