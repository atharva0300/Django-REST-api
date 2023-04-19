from django.db import models

# Create your models here.
class Typing(models.Model) : 
    duration = models.IntegerField()
    difficulty = models.TextField()
    displayText = models.TextField()
    inputText = models.TextField()
