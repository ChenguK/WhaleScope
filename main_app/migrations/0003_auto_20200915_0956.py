# Generated by Django 3.1.1 on 2020-09-15 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sighting_species'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sighting',
            options={'ordering': ['-date']},
        ),
    ]