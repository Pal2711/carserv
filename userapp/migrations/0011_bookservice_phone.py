# Generated by Django 4.2 on 2025-05-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_bookservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookservice',
            name='phone',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]
