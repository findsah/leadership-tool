# Generated by Django 4.1.7 on 2023-04-22 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondtoll', '0005_alter_questionoption_answer_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='can_multiple_choice',
            field=models.BooleanField(default=False, verbose_name='Can select multiple options?'),
        ),
        migrations.AddField(
            model_name='question',
            name='can_skip',
            field=models.BooleanField(default=False, verbose_name='Can skip this Questions?'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.CharField(default='', max_length=10),
        ),
    ]
