# Generated by Django 3.0.6 on 2020-10-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0005_auto_20201017_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='rank1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='rank2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='rank3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='rank4',
            field=models.TextField(blank=True, null=True),
        ),
    ]