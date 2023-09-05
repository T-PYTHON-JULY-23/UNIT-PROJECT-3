# Generated by Django 4.2.4 on 2023-09-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('consultation', 'consultation'), ('training', 'training'), ('making activities', 'making activities'), ('phone reapire', 'phone reapire')], max_length=256)),
                ('image', models.ImageField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
