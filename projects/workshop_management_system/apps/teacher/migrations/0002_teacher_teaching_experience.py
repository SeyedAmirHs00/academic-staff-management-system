# Generated by Django 5.0.1 on 2024-01-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teaching_experience',
            field=models.IntegerField(default=0, verbose_name='teaching experience'),
        ),
    ]
