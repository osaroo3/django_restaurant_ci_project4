# Generated by Django 4.2.11 on 2024-03-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatery', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='table_choice',
            field=models.CharField(choices=[('Table for 1', 'Table for 1'), ('Table for 2', 'Table for 2'), ('Table for 4', 'Table for 4'), ('Table for 6', 'Table for 6'), ('Table for 8', 'Table for 8')], default='Table for 1', max_length=50),
        ),
    ]
