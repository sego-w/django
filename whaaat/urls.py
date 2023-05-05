from django.urls import path, include
from . import views
from base.views import home, register, user_login, logout_view, FileUploadView, SummaryView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('summary/', SummaryView.as_view(), name='summary'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)