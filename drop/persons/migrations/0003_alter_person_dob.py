# Generated by Django 4.2.1 on 2023-05-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DOB',
            field=models.DateField(blank=True),
        ),
    ]