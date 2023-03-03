from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.TextField()


class Segment(models.Model):
    name = models.CharField(max_length=255)
    intercept = models.FloatField()

    def __str__(self):
        return self.name


# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     value = models.CharField(max_length=255, choices=(
#         ('sd', 'Strongly Disagree'),
#         ('d', 'Disagree'),
#         ('n', 'Neither agree nor disagree'),
#         ('a', 'Agree'),
#         ('sa', 'Strongly Agree')
#     ))
#
#     def __str__(self):
#         return f'{self.user} - {self.question} - {self.value}'


class Response(models.Model):
    user_id = models.IntegerField()
    ANSWER_CHOICES = [
        ('SD', 'Strongly Disagree'),
        ('D', 'Disagree'),
        ('N', 'Neither Agree Nor Disagree'),
        ('A', 'Agree'),
        ('SA', 'Strongly Agree'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2, choices=ANSWER_CHOICES)

    def __str__(self):
        return f"{self.question}: {self.get_answer_display()}"


class LeadershipType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserSegment(models.Model):
    user_id = models.IntegerField()
    leadership_type = models.ForeignKey(LeadershipType, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.user_id} - {self.leadership_type}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user.username + " - " + self.plan.name


class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.user} - {self.membership_type}'
