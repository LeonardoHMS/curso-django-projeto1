# Generated by Django 4.2 on 2023-07-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0007_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default='14/07/2023'),
        ),
    ]
