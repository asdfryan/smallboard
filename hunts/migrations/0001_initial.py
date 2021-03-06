# Generated by Django 2.2.7 on 2019-11-25 01:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('puzzlers', models.ManyToManyField(related_name='hunts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
