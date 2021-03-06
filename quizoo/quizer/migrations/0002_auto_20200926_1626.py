# Generated by Django 3.1.1 on 2020-09-26 16:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersgivingtest',
            name='question_attempted',
        ),
        migrations.AddField(
            model_name='usersgivingtest',
            name='question_not_attempted',
            field=models.CharField(default=(1, 2), max_length=2000, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='question_list'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_list', to='quizer.quiz'),
        ),
    ]
