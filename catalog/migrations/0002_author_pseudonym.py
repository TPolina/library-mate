# Generated by Django 4.0.3 on 2022-04-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
