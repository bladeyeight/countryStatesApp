# Generated by Django 4.2.10 on 2024-02-26 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_state_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='country',
            new_name='countryId',
        ),
    ]
