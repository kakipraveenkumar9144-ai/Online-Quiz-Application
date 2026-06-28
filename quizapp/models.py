from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    question = models.CharField(max_length=300)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    answer = models.CharField(max_length=200)

    question_no = models.IntegerField(default=1)

    def __str__(self):
        return self.question


class Result(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username