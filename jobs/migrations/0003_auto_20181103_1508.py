# Generated by Django 2.1.2 on 2018-11-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181103_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagetemp2',
            new_name='image',
        ),
    ]
