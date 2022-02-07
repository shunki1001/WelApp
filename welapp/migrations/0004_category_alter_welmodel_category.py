# Generated by Django 4.0.2 on 2022-02-05 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welapp', '0003_welmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('KT', 'Kitchen'), ('BT', 'Bath'), ('RM', 'Room'), ('CO', 'Cook'), ('AM', 'Amenity'), ('OT', 'Other')], default='KT', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='welmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welapp.category'),
        ),
    ]