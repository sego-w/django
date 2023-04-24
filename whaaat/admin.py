from django.contrib import admin
from django.contrib import admin
from whaaat.models import File, FileType

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ["maksja", 'maksesaaja', 'summa']
admin.site.register(File, FileAdmin)