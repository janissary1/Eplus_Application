# Generated by Django 2.2.4 on 2019-11-09 18:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eplus_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Running',
            new_name='Process',
        ),
    ]
