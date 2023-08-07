# Generated by Django 4.2.3 on 2023-07-03 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=150)),
                ('create', models.DateField(auto_now_add=True)),
                ('uploded_at', models.DateField(auto_now=True)),
                ('draft', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=50)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='post')),
            ],
        ),
    ]
