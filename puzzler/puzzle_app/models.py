from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'puzzle_app'

class Score(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.question} - {self.answer} - {self.score}"
    
    class Meta:
        app_label = 'puzzle_app'