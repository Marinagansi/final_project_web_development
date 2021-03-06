# Generated by Django 4.0 on 2022-01-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloths',
            fields=[
                ('cloth_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('cloth_name', models.CharField(max_length=200)),
                ('cloth_type', models.CharField(max_length=200)),
                ('cloth_details', models.CharField(max_length=200)),
                ('flight_way', models.CharField(max_length=100)),
                ('cloth_price', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'cloths',
            },
        ),
    ]
