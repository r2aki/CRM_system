from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False, label='Телефон')
    middle_name = forms.CharField(max_length=50, required=False, label='Отчество')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone')


class CustomUserChangeForm(UserChangeForm):
    phone = forms.CharField(max_length=20, required=False, label='Телефон')
    middle_name = forms.CharField(max_length=50, required=False, label='Отчество')

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'phone')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']