# Generated by Django 4.1.7 on 2023-04-18 12:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_leadershiptype_external_links_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadershiptype',
            name='description6',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description7',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description8',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='leadershiptype',
            name='description9',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='You Might also like'),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='leadershiptype',
            name='description5',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
