# Generated by Django 3.2.4 on 2021-09-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_callback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleinfo',
            old_name='image',
            new_name='vehicleImage',
        ),
    ]