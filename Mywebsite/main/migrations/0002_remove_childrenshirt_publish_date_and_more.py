# Generated by Django 4.2.4 on 2023-09-03 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childrenshirt',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='shirt',
            name='publish_date',
        ),
    ]
