# Generated by Django 2.1.5 on 2022-02-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20220204_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slgu',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]