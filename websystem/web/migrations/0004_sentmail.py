# Generated by Django 3.2.6 on 2022-11-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_threshold_weatherpred'),
    ]

    operations = [
        migrations.CreateModel(
            name='sentmail',
            fields=[
                ('sentmailID', models.AutoField(primary_key=True, serialize=False)),
                ('sentmail', models.BooleanField()),
            ],
        ),
    ]
