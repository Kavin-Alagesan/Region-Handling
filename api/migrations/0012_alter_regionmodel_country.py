# Generated by Django 4.1 on 2022-08-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_regionmodel_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='country',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'India'), ('2', 'USA'), ('3', 'Japan'), ('4', 'China'), ('5', 'Cambodia'), ('6', 'Rwanda'), ('7', 'Thailand')], max_length=30),
        ),
    ]
