# Generated by Django 5.0.1 on 2024-04-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likecount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
