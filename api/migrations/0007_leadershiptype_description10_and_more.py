# Generated by Django 4.1.7 on 2023-04-19 11:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_leadershiptype_description6_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadershiptype',
            name='description10',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description11',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description12',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description13',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description14',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='You Might also like'),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description15',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='You Might also like'),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description9',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]