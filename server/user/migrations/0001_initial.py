# Generated by Django 4.1.1 on 2023-01-24 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qname', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('type', models.CharField(max_length=10)),
                ('points', models.SmallIntegerField()),
                ('const1', models.TextField()),
                ('const2', models.TextField()),
                ('testcaseinput1', models.TextField()),
                ('testcaseoutput1', models.TextField()),
                ('testcaseinput2', models.TextField()),
                ('testcaseoutput2', models.TextField()),
                ('testcaseinput3', models.TextField()),
                ('testcaseoutput3', models.TextField()),
                ('testcaseinput4', models.TextField()),
                ('testcaseoutput4', models.TextField()),
                ('testcaseinput5', models.TextField()),
                ('testcaseoutput5', models.TextField()),
                ('testcaseinput6', models.TextField()),
                ('testcaseoutput6', models.TextField()),
                ('testcaseinput7', models.TextField()),
                ('testcaseoutput7', models.TextField()),
                ('testcaseinput8', models.TextField()),
                ('testcaseoutput8', models.TextField()),
                ('testcaseinput9', models.TextField()),
                ('testcaseoutput9', models.TextField()),
                ('testcaseinput10', models.TextField()),
                ('testcaseoutput10', models.TextField()),
                ('testcaseinput11', models.TextField()),
                ('testcaseoutput11', models.TextField()),
                ('testcaseinput12', models.TextField()),
                ('testcaseoutput12', models.TextField()),
                ('testcaseinput13', models.TextField()),
                ('testcaseoutput13', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('year', models.SmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('tname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('duration', models.TimeField(default=None)),
                ('starttime', models.DateTimeField(default=None)),
                ('endtime', models.DateTimeField(default=None)),
                ('question', models.ManyToManyField(to='user.question')),
                ('student', models.ManyToManyField(to='user.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('starttime', models.DateTimeField(blank=True, default=None, null=True)),
                ('endtime', models.DateTimeField(blank=True, default=None, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.test')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_score', models.IntegerField()),
                ('precision', models.FloatField()),
                ('recall', models.FloatField()),
                ('qname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.question')),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.test')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('time', models.DurationField()),
                ('rank', models.IntegerField(default=None)),
                ('total_precision', models.FloatField(default=None)),
                ('total_recall', models.FloatField(default=None)),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
                ('tname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.test')),
            ],
        ),
    ]
