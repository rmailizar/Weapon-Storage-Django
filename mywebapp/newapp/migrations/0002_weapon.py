# Generated by Django 5.0.6 on 2024-05-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('tipe', models.CharField(max_length=100)),
                ('jumlah', models.IntegerField()),
            ],
        ),
    ]
