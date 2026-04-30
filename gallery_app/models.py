from django.db import models

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Quiz', 'Quiz'),
        ('Workshop', 'Workshop'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)  
    date_captured = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} - {self.category}"
