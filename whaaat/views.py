from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from serializers import FileUploadSerializer, SaveFileSerializer
from models import File

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