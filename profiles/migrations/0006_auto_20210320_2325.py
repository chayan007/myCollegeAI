# Generated by Django 3.1.5 on 2021-03-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210318_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpverification',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
