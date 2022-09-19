# Generated by Django 4.1 on 2022-08-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_region_name_regionmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='country',
            field=models.CharField(choices=[('0', 'Unknown'), ('1', 'India'), ('2', 'USA'), ('3', 'Japan'), ('4', 'China'), ('5', 'Cambodia'), ('6', 'Rwanda'), ('7', 'Thailand')], default='Unknown', max_length=30),
        ),
    ]