# Generated by Django 3.0.4 on 2020-08-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='class_name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
