# Generated by Django 2.1.5 on 2022-02-04 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_slgu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slgu',
            new_name='slug',
        ),
    ]
