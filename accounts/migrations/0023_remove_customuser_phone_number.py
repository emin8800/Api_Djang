# Generated by Django 5.1.1 on 2024-10-07 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_customuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
    ]
