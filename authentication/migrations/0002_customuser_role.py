# Generated by Django 5.0.2 on 2024-03-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
