# Generated by Django 4.2.11 on 2024-03-25 09:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eatery', '0004_alter_booking_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('user', 'date', 'time', 'menu')},
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together={('menu_name', 'price')},
        ),
    ]
