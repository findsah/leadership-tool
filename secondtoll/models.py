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
    question_slug = models.SlugField(unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    def save(self, *args, **kwargs):
        if Question.objects.filter(question_text=self.question_text).exists():
            extra = str(randint(1, 10000))
            self.question_slug = slugify(self.question_text) + "-" + extra
        else:
            self.question_slug = slugify(self.question_text) 
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_text

class QuestionOption(models.Model): 
    question = models.ForeignKey(Question, related_name='question_answers', on_delete=models.CASCADE, null=True)
    answer_test = models.CharField(max_length=100, verbose_name='Options', default='')  

    def __str__(self):
        return self.question.question_text
    
# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
#     question = models.ForeignKey(Question, related_name='question_answers')
#     answer_test = models.CharField(max_length=100, verbose_name='Options', default='') 
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 

#     def __str__(self):
#         return self.question.question_text