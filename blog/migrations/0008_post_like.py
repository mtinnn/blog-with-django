# Generated by Django 4.2.3 on 2023-07-21 01:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
