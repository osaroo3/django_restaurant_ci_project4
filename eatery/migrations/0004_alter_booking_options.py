# Generated by Django 4.2.11 on 2024-03-22 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatery', '0003_booking_table_choice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_on']},
        ),
    ]
