# Generated by Django 4.1 on 2022-08-19 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_region_code_regionmodel_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regionmodel',
            old_name='region_name',
            new_name='name',
        ),
    ]