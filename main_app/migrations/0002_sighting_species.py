# Generated by Django 3.1 on 2020-09-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='species',
            field=models.CharField(choices=[('1', 'Orca'), ('2', 'Minke'), ('3', 'Humpback'), ('4', 'Dolphin'), ('5', 'Seal'), ('6', 'Sea Lion'), ('7', 'Sea Otter'), ('8', 'Other'), ('9', 'Unknown')], default='1', max_length=1),
        ),
    ]