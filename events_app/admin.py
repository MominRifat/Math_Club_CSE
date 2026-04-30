from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_registration', 'end_registration', 'current_status')
    list_filter = ('event_type', 'is_published')

    def current_status(self, obj):
        return obj.get_status()