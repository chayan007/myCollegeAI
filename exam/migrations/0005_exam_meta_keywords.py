# Generated by Django 3.1.5 on 2021-06-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20210623_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='meta_keywords',
            field=models.JSONField(blank=True, default=[], null=True),
        ),
    ]
