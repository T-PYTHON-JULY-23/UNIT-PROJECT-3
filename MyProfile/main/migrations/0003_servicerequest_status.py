# Generated by Django 4.2.4 on 2023-09-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_service_image_servicerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'in_progress'), (3, 'done'), (4, 'canceled')], default=1),
            preserve_default=False,
        ),
    ]
