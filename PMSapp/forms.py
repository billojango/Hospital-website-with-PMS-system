from django import forms
from PMSapp.models import Patient, ImageModel, Payment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phone', 'amount']