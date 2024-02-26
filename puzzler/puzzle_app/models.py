from django.db import models

# Create your models here.

# API TO USE LATER: https://opentdb.com/api.php?amount=1

class Quiz(models.Model):
    title = models.CharField(max_length=255)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class Player(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name