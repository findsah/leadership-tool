from django.contrib import admin
from .models import Question, QuestionOption, Category, UserAnswer
# Register your models here.

class QuestionOption_Admin(admin.TabularInline):
    model=QuestionOption

class Question_Admin(admin.ModelAdmin):
    inlines = [QuestionOption_Admin] 

admin.site.register(Question, Question_Admin)
admin.site.register(QuestionOption)
admin.site.register(Category)
admin.site.register(UserAnswer)