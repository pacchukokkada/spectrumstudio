# Generated by Django 3.0.8 on 2020-08-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0011_auto_20200812_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allphoto',
            name='photo_type',
            field=models.CharField(choices=[('Commercial', 'Commercial'), ('Kids', 'Kids'), ('Portrait', 'Portrait')], max_length=10),
        ),
    ]
