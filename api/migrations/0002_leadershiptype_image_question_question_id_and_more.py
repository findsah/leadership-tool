# Generated by Django 4.1.7 on 2023-04-04 01:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadershiptype',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='name',
            field=models.CharField(choices=[('Careful Collaborator', 'Careful Collaborator'), ('Methodical Specialist', 'Methodical Specialist'), ('Culture Creator', 'Culture Creator'), ('Intuitive Decider', 'Intuitive Decider'), ('Determined Driver', 'Determined Driver'), ('Collective Adventurer', 'Collective Adventurer')], max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.CharField(choices=[('-2', 'Strongly Disagree'), ('-1', 'Disagree'), ('0', 'Neither Agree Nor Disagree'), ('1', 'Agree'), ('2', 'Strongly Agree')], max_length=2),
        ),
    ]
