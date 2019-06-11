from django import forms

from ..formfields import PhoneNumberField

from .models import NullablePhoneNumber


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = NullablePhoneNumber
        fields = ["phone_number"]


class CustomPhoneNumberFormField(PhoneNumberField):
    pass
