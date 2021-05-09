# Generated by Django 2.2 on 2020-05-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_delete_rented_bikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rented_Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('bike', models.CharField(max_length=20, null=True)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
    ]
