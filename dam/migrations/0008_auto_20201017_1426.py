# Generated by Django 3.0.6 on 2020-10-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0007_auto_20201017_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='department2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='department',
            field=models.TextField(blank=True, null=True),
        ),
    ]