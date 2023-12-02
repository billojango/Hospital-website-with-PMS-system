from django import forms
from PMSapp.models import Patient, ImageModel, Payment, Member


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

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'username', 'password', 'passwordconfirm']
        widgets = {
            'password': forms.PasswordInput(),
            'passwordconfirm': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('passwordconfirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data