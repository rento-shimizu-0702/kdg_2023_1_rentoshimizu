from django.db import models

# Create your models here.

class Shioriha_Profile(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.title
    