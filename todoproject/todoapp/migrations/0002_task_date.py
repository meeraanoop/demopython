# Generated by Django 4.2.11 on 2024-03-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-02-22'),
            preserve_default=False,
        ),
    ]
