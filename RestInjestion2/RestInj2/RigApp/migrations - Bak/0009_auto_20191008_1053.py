# Generated by Django 2.0.13 on 2019-10-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RigApp', '0008_auto_20191008_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rig',
            old_name='raw_data_file',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='rig',
            old_name='notes',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='rig',
            old_name='well_bore_diameter',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='rig',
            old_name='rig_location',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='rig',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
