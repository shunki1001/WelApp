# Generated by Django 4.0.2 on 2022-02-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='welmodel',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]