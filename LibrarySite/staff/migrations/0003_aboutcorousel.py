# Generated by Django 4.1.7 on 2023-03-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_home_image_alter_home_line_1_alter_home_line_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCorousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
            ],
        ),
    ]
