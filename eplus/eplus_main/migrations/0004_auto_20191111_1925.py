# Generated by Django 2.2.4 on 2019-11-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eplus_main', '0003_auto_20191111_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='progress',
            field=models.FloatField(),
        ),
    ]