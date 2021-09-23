from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    class Meta:
        #group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]
        labels = {
            'username': 'Nombre usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Email',
            'password1':'Contraseña',
            'password2':'Confirmar Contraseña',
            }

"""class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name","last_name","email","password1","password2,groups"]
        """