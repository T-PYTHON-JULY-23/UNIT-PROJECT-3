# Generated by Django 4.2.4 on 2023-09-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.TextField(choices=[('pending', 'pending'), ('in_progress', 'in_progress'), ('done', 'done'), ('canceled', 'canceled')], default='pending'),
        ),
    ]
