# Generated by Django 4.0.5 on 2022-07-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bis_app', '0009_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='post',
        ),
    ]
