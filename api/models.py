from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_id = models.SlugField(max_length=50, unique=True, default='')
    question_text = models.TextField()
    def __str__(self):
        return self.question_text

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


class UserAnswer(models.Model):
    user_id = models.IntegerField()
    ANSWER_CHOICES = [
        ('1', 'Strongly Disagree'),
        ('2', 'Disagree'),
        ('3', 'Neither Agree Nor Disagree'),
        ('4', 'Agree'),
        ('5', 'Strongly Agree'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2, choices=ANSWER_CHOICES)

    def __str__(self):
        return f"{self.question}: {self.get_answer_display()}"


class LeadershipType(models.Model):
    LEADERSHIP_TYPE = [
                ('Careful Collaborator', 'Careful Collaborator'),
                ('Methodical Specialist', 'Methodical Specialist'),
                ('Culture Creator', 'Culture Creator'),
                ('Intuitive Decider', 'Intuitive Decider'),
                ('Determined Driver', 'Determined Driver'),
                ('Collective Adventurer', 'Collective Adventurer'),
            ]
            
    name = models.CharField(max_length=50, choices=LEADERSHIP_TYPE, unique=True)
    title = models.CharField(max_length=255, blank=True)
    description =  RichTextUploadingField() 
    description2 = RichTextUploadingField(blank=True)
    description3 = RichTextUploadingField(blank=True)
    description4 = RichTextUploadingField(blank=True)
    description5 = RichTextUploadingField(blank=True)
    description6 = RichTextUploadingField(blank=True)
    description7 = RichTextUploadingField(blank=True)
    description8 = RichTextUploadingField(blank=True)
    description9 = RichTextUploadingField(blank=True)
    description10 = RichTextUploadingField(blank=True)
    description11 = RichTextUploadingField(blank=True)
    description12 = RichTextUploadingField(blank=True)
    description13 = RichTextUploadingField(blank=True) 
    description14 = RichTextUploadingField(blank=True,verbose_name=_("You Might also like")) 
    description15 = RichTextUploadingField(blank=True,verbose_name=_("You Might also like")) 
    external_links=models.TextField(blank=True, 
                                    help_text=mark_safe(_(
                                    '<p><b style="color:orange">Note: </b>Please enter all links comma seprated.</p>'
                                    ))
                            )
    external_links_text=models.TextField(blank=True, 
                                         help_text = 
                                         mark_safe(_(
                                        '<p><b style="color:orange">Note: </b>Please enter diplay text for the links in same order(External links) with comma seprated.</p>'
                                         ))
                                    )
    # description = RichTextUploadingField()
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
 
    def get_image(self):
        if self.image:
            return 'https://walrus-app-xqntt.ondigitalocean.app'+self.image.url
        return ''

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
