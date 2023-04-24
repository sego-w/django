from django.contrib import admin
from django.contrib import admin
from models import File, FileType

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "staff_name", "position", "age",   "year_joined"]
admin.site.register(File, FileAdmin)