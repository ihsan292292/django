# Generated by Django 3.2.8 on 2022-05-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sadds', models.CharField(max_length=100)),
                ('scity', models.CharField(max_length=100)),
                ('semail', models.CharField(max_length=100)),
                ('sphon', models.IntegerField()),
                ('sgender', models.CharField(max_length=1)),
            ],
        ),
    ]