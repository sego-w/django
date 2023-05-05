from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse
from base.forms import RegistrationForm, LoginForm
import csv
from .models import Payment
from django.contrib import messages
from .forms import FileUploadForm
from .utils import parse_csv_file
from django.views import View

# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer


"""from django.contrib.auth.models import User

user = User.objects.create_user("peeter", "peeter@mail.com", "peeter123")"""

# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def room(request):
    return HttpResponse('ROOM')




class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                       maksja = row['Maksja'],
                       maksesaaja = row["Makse saaja"],
                       summa = row["Age"],
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
    
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('logout_confirm')
    
@login_required
def logout_confirm(request):
    return render(request, 'logout_confirm.html')


class SummaryView(View):
    def get(self, request):
        payments = Payment.objects.all()
        summary = {}
        for payment in payments:
            if payment.payer not in summary:
                summary[payment.payer] = 0
            if payment.payee not in summary:
                summary[payment.payee] = 0
            summary[payment.payer] -= payment.amount
            summary[payment.payee] += payment.amount
        return render(request, 'summary.html', {'summary': summary})
    

class FileUploadView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'file_upload.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():




            print('Form is valid')





            payments = parse_csv_file(request.FILES['file'])
            Payment.objects.bulk_create(payments)
            messages.success(request, 'Upload successful')
            return redirect('summary')
        else:




            print('Form is not valid')





            messages.error(request, 'Invalid file')
        return render(request, 'file_upload.html', {'form': form})