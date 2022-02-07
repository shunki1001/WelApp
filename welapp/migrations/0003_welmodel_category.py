# Generated by Django 4.0.2 on 2022-02-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welapp', '0002_welmodel_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='welmodel',
            name='category',
            field=models.CharField(choices=[('KT', 'Kitchen'), ('BT', 'Bath'), ('RM', 'Room'), ('CO', 'Cook'), ('AM', 'Amenity'), ('OT', 'Other')], default='KT', max_length=2),
        ),
    ]