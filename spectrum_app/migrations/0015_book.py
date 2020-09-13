# Generated by Django 3.0.8 on 2020-08-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0014_auto_20200813_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('shoot_type', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]