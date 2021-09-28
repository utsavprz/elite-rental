# Generated by Django 3.2.4 on 2021-09-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_paymentgateway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstantly',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Done', 'Done')], default='Processing', max_length=150),
        ),
    ]
