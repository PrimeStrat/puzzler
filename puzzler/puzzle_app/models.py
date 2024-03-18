from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name