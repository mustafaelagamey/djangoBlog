# Generated by Django 3.2.7 on 2021-11-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
    ]
