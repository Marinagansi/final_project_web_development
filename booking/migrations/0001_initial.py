# Generated by Django 4.0 on 2022-01-24 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('cloths', '0002_remove_cloths_flight_way'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('days', models.CharField(max_length=50)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloths.cloths')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
