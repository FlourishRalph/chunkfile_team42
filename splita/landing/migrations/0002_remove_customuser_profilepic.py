# Generated by Django 4.0.6 on 2022-08-07 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profilepic',
        ),
    ]
