# Generated by Django 4.1.7 on 2023-04-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_bookstoppicks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
