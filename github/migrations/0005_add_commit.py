# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0004_add_pr_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.CharField(db_index=True, max_length=40)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('url', models.URLField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='github.Repository')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='github.User')),
            ],
        ),
        migrations.AlterField(
            model_name='pullrequest',
            name='state',
            field=models.IntegerField(choices=[(10, 'Open'), (100, 'Closed')], default=10),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='merge_commit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pull_requests', to='github.Commit'),
        ),
    ]
