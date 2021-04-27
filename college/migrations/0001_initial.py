# Generated by Django 3.1.4 on 2020-12-21 14:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('abbreviated_name', models.CharField(max_length=50, null=True)),
                ('meta', models.TextField(null=True)),
                ('keywords', models.TextField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('brochure', models.FileField(null=True, upload_to='college/brochure/')),
                ('image', models.ImageField(null=True, upload_to='college/image/')),
                ('logo', models.ImageField(null=True, upload_to='college/logo/')),
                ('ownership', models.IntegerField(choices=[(0, 'Private'), (1, 'Public'), (2, 'Other')], null=True)),
                ('approval', models.CharField(max_length=100, null=True)),
                ('college_type', models.IntegerField(choices=[(0, 'Graduation College'), (1, 'Diploma College'), (2, 'Vocational Training')], null=True)),
                ('established_year', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(null=True)),
                ('about', models.TextField(null=True)),
                ('is_top', models.SmallIntegerField(default=0, null=True)),
                ('admission_process', models.TextField(null=True)),
                ('placements', models.TextField(null=True)),
                ('degrees', models.JSONField(null=True)),
                ('stream_degree', models.JSONField(null=True)),
                ('streams', models.JSONField(null=True)),
                ('entrance_exams', models.JSONField(null=True)),
                ('contacts', models.JSONField(null=True)),
                ('images', models.JSONField(null=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
