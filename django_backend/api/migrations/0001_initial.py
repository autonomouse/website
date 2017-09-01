# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('created_at', models.DateTimeField(blank=True, default=None, help_text='DateTime this model instance was created.', null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime this model instance was last updated.')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='About', help_text='Name of page.', max_length=255, unique=True)),
                ('priority', models.IntegerField(default=0, help_text='Reverse order which pages appear in the UI (0 first).')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('created_at', models.DateTimeField(blank=True, default=None, help_text='DateTime this model instance was created.', null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime this model instance was last updated.')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Introduction', help_text='Name of section.', max_length=255, unique=True)),
                ('priority', models.IntegerField(default=0, help_text='Reverse order which sections appear in the UI (0 first).')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='api.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('created_at', models.DateTimeField(blank=True, default=None, help_text='DateTime this model instance was created.', null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='DateTime this model instance was last updated.')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('priority', models.IntegerField(default=0, help_text='Reverse order which statements appear in the UI (0 first).')),
                ('title', models.CharField(help_text='Statement title.', max_length=255)),
                ('text', models.TextField(blank=True, default=None, help_text='The text of the statement.', null=True)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statements', to='api.Section')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
