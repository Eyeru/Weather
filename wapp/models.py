from django.db import models

# Create your models here.
class Weather(models.Model):
    area = models.CharField(max_length=200)

    def __str__(self):
        return self.area
