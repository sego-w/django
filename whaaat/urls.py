from django.urls import path
from . import views
from files.views import UploadFileView

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('upload/', UploadFileView.as_view(), name='upload-file')
]



