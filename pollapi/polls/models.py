
import datetime
from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return self.name

class Question(models.Model):
    survey = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created"]
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    VAL1 = '1'
    VAL2 = '2'
    VAL3 = '3'
    VAL4 = '4'
    VAL5 = '5'

    MULTICHOICE = [
        (VAL1, 'least'),
        (VAL2, 'less_than_average'),
        (VAL3, 'average'),
        (VAL4, 'more_than_average'),
        (VAL5, 'most'),
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    votes = models.CharField(choices=MULTICHOICE,default=0,max_length=2)
    #yesno =models.CharField(choices=YES_NO_CHOICES, default=0, max_length=2)

    def __str__(self):
     return self.choice_text

   