# Generated by Django 4.2.4 on 2023-09-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Service/'),
        ),
    ]
