# Generated by Django 3.2.6 on 2022-10-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20221007_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='CreationDate',
            field=models.DateTimeField(default='07.10.2022 20:42:18'),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='Temperature',
            field=models.FloatField(),
        ),
    ]