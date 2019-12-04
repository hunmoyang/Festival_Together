# Generated by Django 2.1 on 2019-12-03 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20191202_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(default='', max_length=50)),
                ('user_id', models.CharField(default='', max_length=20)),
                ('date', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(default='', max_length=100)),
                ('leader_id', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
