# Generated by Django 4.0.4 on 2022-05-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='std',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('m1', models.CharField(max_length=100)),
                ('m2', models.CharField(max_length=100)),
                ('m3', models.CharField(max_length=100)),
                ('total_mark', models.CharField(max_length=100)),
                ('avg_mark', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
            ],
        ),
    ]
