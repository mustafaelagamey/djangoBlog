# Generated by Django 3.2.7 on 2021-10-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_comment_commenter_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation_datetime',
            new_name='creation',
        ),
        migrations.AddField(
            model_name='comment',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, default='2021-10-22 12:00:00'),
            preserve_default=False,
        ),
    ]
