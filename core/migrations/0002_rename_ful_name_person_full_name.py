# Generated by Django 4.0.3 on 2022-04-19 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='ful_name',
            new_name='full_name',
        ),
    ]