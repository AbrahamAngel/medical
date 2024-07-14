from django.contrib import admin
from med.models import Patient

@admin.register(Patient)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
