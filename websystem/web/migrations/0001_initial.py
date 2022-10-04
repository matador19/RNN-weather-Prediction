# Generated by Django 4.1 on 2022-10-04 15:58

import datetime
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
            name='Ticket',
            fields=[
                ('TicketId', models.AutoField(primary_key=True, serialize=False)),
                ('CreationDate', models.DateTimeField(default='04.10.2022 18:58:12')),
                ('Status', models.BooleanField()),
                ('Initiator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('LogId', models.AutoField(primary_key=True, serialize=False)),
                ('CreationDate', models.DateTimeField(default=datetime.datetime(2022, 10, 4, 18, 58, 12, 184362))),
                ('Change', models.TextField()),
                ('Type', models.CharField(max_length=20)),
                ('Initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.BigIntegerField(blank=True, null=True)),
                ('Role', models.CharField(choices=[('Admin', 'Admin'), ('Supervisor', 'Supervisor')], max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
