from django.db import models

# Create your models here.
class Click(models.Model):
    clicks = models.PositiveIntegerField()