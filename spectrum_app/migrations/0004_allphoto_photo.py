# Generated by Django 3.0.8 on 2020-08-04 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum_app', '0003_auto_20200804_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=50)),
                ('photo_type', models.CharField(choices=[('Commercial', 'Commercial'), ('Kids', 'Kids'), ('Potrait', 'Potrait')], max_length=10)),
                ('c_man', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spectrum_app.AllPhoto')),
            ],
        ),
    ]
