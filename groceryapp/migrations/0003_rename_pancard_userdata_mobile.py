# Generated by Django 4.2.5 on 2024-03-12 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0002_remove_userdata_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='PanCard',
            new_name='Mobile',
        ),
    ]
