# Generated by Django 4.1.5 on 2023-01-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]