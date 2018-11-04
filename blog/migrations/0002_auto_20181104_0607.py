# Generated by Django 2.1.2 on 2018-11-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='text',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]