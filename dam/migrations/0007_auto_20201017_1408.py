# Generated by Django 3.0.6 on 2020-10-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0006_auto_20201017_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='education',
            name='school',
        ),
        migrations.AddField(
            model_name='education',
            name='department',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='high_school',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='middle_shool',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='primary_shool',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='programme',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='remarks1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='remarks2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='remarks3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='university',
            field=models.TextField(blank=True, null=True),
        ),
    ]
