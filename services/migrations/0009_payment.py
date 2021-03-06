# Generated by Django 3.2.4 on 2021-09-27 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0008_rename_image_vehicleinfo_vehicleimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=150)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.bookinstantly')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.vehicleinfo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
