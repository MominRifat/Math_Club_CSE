from django.shortcuts import render
from .models import Event
from django.utils import timezone
from django.core.paginator import Paginator

def events(request):
    now = timezone.now()
    all_qs = Event.objects.filter(is_published=True)
    running_events = [e for e in all_qs if e.start_registration <= now <= e.end_registration]
    upcoming_events = [e for e in all_qs if e.start_registration > now]
    finished_events = [e for e in all_qs if e.end_registration < now]
    running_events.sort(key=lambda x: x.start_registration, reverse=True)
    upcoming_events.sort(key=lambda x: x.start_registration, reverse=True)
    finished_events.sort(key=lambda x: x.start_registration, reverse=True)
    sorted_events = running_events + upcoming_events + finished_events
    for event in sorted_events:
        event.status = event.get_status()
    paginator = Paginator(sorted_events, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events_app/events.html', {'events': page_obj, 'now': now})