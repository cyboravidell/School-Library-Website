# Generated by Django 4.1.7 on 2023-03-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=100)),
                ('line_1', models.CharField(max_length=150)),
                ('line_2', models.CharField(max_length=140)),
                ('line_3', models.CharField(max_length=140)),
            ],
        ),
    ]
