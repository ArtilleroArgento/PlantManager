from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    origin_zone = models.CharField(max_length=100)
    care_instructions = models.TextField()

   

