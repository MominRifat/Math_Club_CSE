
from django.db import models
from django.utils import timezone

class Event(models.Model):
    EVENT_TYPES = [
        ('MATH_OLYMPIAD', 'Math Olympiad'),
        ('PUZZLE_HUNT', 'Puzzle Hunt'),
        ('OTHER', 'Other Event'),
    ]

    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    
    start_registration = models.DateTimeField()
    end_registration = models.DateTimeField()
    
    form_url = models.CharField(max_length=500, help_text="Link to the registration form")
    
    is_published = models.BooleanField(default=True)

    def get_status(self):
        now = timezone.now()
        if now < self.start_registration:
            return "UPCOMING"
        elif self.start_registration <= now <= self.end_registration:
            return "RUNNING"
        else:
            return "FINISHED"

    def __str__(self):
        return self.title