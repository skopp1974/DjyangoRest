# Generated by Django 2.0.13 on 2019-10-08 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RigApp', '0006_auto_20191008_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rig',
            old_name='rig_number',
            new_name='id',
        ),
    ]
