# Generated by Django 4.1.7 on 2023-04-01 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
