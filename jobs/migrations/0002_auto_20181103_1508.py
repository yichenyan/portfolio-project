# Generated by Django 2.1.2 on 2018-11-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='imagetemp2',
        ),
    ]