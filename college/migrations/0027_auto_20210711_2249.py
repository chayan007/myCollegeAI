# Generated by Django 3.1.5 on 2021-07-11 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0026_auto_20210711_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegegenres',
            name='image',
        ),
        migrations.RemoveField(
            model_name='collegegenres',
            name='url_tag',
        ),
    ]
