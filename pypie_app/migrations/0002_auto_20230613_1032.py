# Generated by Django 2.2.4 on 2023-06-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pypie_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pypie',
            name='description',
        ),
        migrations.AddField(
            model_name='pypie',
            name='crust',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pypie',
            name='filling',
            field=models.CharField(default='no_filling', max_length=255),
            preserve_default=False,
        ),
    ]
