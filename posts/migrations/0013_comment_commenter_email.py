# Generated by Django 3.2.7 on 2021-10-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenter_email',
            field=models.EmailField(default='empty@empty.empty', max_length=80),
            preserve_default=False,
        ),
    ]