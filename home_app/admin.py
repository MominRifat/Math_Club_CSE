from django.contrib import admin
from .models import Convenor


@admin.register(Convenor)
class ConvenorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'organization')