# Generated by Django 3.1.1 on 2020-10-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0009_auto_20201001_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
