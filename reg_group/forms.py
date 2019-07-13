from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from reg_group.models import User


class AgencySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agency = True
        if commit:
            user.save()
        return user


class ClientSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        #if commit:
        user.save()
        return user


class VendorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        #if commit:
        user.save()
        return user

