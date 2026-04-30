from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    is_active = models.BooleanField(default=True)
    is_former_president = models.BooleanField(default=False)
    tenure_year = models.CharField(max_length=50, blank=True, help_text="e.g. 2023")
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField(blank=True) 
    dateofbirth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"
