# Generated by Django 3.0.5 on 2020-04-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200418_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='Aprašymas'),
        ),
    ]