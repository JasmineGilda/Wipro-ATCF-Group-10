# Generated by Django 4.1.1 on 2023-01-25 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_test_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='rank',
        ),
    ]