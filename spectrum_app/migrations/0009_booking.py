# Generated by Django 3.0.8 on 2020-08-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0008_weddingcouple_weddingphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('shoot_type', models.CharField(choices=[('Wedding', 'Wedding'), ('Potrait', 'Potrait'), ('Other events', 'Other events')], max_length=20)),
                ('shoot_date', models.DateField()),
                ('days', models.CharField(max_length=4)),
                ('other_info', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
