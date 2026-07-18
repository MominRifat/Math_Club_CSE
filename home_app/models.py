from django.db import models

class Convenor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='convenors/')
    designation = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.name