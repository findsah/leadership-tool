from random import randint
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    group_name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.group_name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField() 
    can_skip = models.BooleanField(default=False, verbose_name='Can skip this Questions?')
    can_multiple_choice = models.BooleanField(default=False, verbose_name='Can select multiple options?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 

    def __str__(self):
        return self.question_text

class QuestionOption(models.Model): 
    question = models.ForeignKey(Question, related_name='question_answers', on_delete=models.CASCADE, null=True)
    answer_test = models.CharField(max_length=500, verbose_name='Options', default='')  

    def __str__(self):
        return self.question.question_text
    
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_value') 
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='question')
    answer = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 

    def __str__(self):
        return (self.question.question_text )