import json

import requests
from django.contrib import messages
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from PMSapp.forms import PatientForm
from PMSapp.models import Member, Patient, ImageModel


from PMSapp.credentials import MpesaAccessToken, LipanaMpesaPpassword,MpesaC2bCredential
from PMSapp.forms import PatientForm, ImageUploadForm, PaymentForm, MemberForm



# Create your views here.

def index(request):
    return render(request,'index.html')

def inner(request):
    return render(request,'inner-page.html')

def login(request):
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['passwordconfirm']

            if password == password_confirm:
                member = form.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')  # Redirect to your login page
            else:
                messages.error(request, 'Passwords do not match')
        else:
            messages.error(request, 'Invalid form submission. Please check your input.')

    else:
        form = MemberForm()

    return render(request, 'registration.html', {'form': form})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def departments(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'doctors.html')

def contacts(request):
    return render(request,'contacts.html')

def appointments(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
            form = PatientForm()
            return render(request,'appointments.html',{'form':form})


def show(request):
    patient = Patient.objects.all()
    return render(request,'show.html',{'patient':patient})


def delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('/show')


def edit(request, id):
    patient = Patient.objects.get(id=id)
    return render(request,'edit.html',{'patient':patient})

def update(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html',{'patient':patient})





def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Beela Referral Hospital",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')


def pay(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_success')  # Redirect to a success page
    else:
        form = PaymentForm()

    return render(request, 'pay.html', {'form': form})