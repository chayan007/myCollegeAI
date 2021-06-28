# Generated by Django 3.1.5 on 2021-06-27 15:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0019_auto_20210618_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeGenres',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='college',
            name='tags',
            field=models.ManyToManyField(to='college.CollegeGenres'),
        ),
    ]