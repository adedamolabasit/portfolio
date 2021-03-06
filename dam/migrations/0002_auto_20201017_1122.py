# Generated by Django 3.0.6 on 2020-10-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.TextField()),
                ('degree', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification1', models.TextField(blank=True, null=True)),
                ('specification2', models.TextField(blank=True, null=True)),
                ('specification3', models.TextField(blank=True, null=True)),
                ('specification4', models.TextField(blank=True, null=True)),
                ('company', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='descriptions',
            new_name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='adedamolabasit09@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default='08108768242'),
            preserve_default=False,
        ),
    ]
