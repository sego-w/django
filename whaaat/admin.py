from django.contrib import admin



# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ["maksja", 'maksesaaja', 'summa']
admin.site.register(File, FileAdmin)