# Generated by Django 5.0 on 2023-12-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='brand',
            new_name='catagory',
        ),
    ]
