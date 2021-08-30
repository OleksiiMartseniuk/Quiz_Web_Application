from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'User with login "{username} not found in the system')
        if not user.check_password(password):
            raise forms.ValidationError("Invalid password")
        return self.cleaned_data


class RegistrationForms(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Name {username} busy. Try something else.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This postal address is already registered!')
        return email
