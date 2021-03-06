# Generated by Django 3.2.4 on 2021-09-22 10:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210917_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinfo',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sunroof', 'Sunroof'), ('GPS', 'GPS'), ('All Wheel drive', 'All Wheel drive'), ('Heated seats', 'Heated seats'), ('Bluetooth', 'Bluetooth'), ('Apple CarPlay', 'Apple CarPlay'), ('Android Auto', 'Android Auto'), ('Backup camera', 'Backup camera'), ('Cruise Control', 'Cruise Control'), ('Push-Button Start', 'Push-Button Start')], max_length=150),
        ),
    ]
