# Generated by Django 4.2.3 on 2023-07-03 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug_alter_post_auth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titel',
            new_name='title',
        ),
    ]