# Generated by Django 3.2.9 on 2021-11-21 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_rename_boot_cause_datapacket_bootcause'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapacket',
            old_name='attitutde_2',
            new_name='attitude_2',
        ),
    ]
