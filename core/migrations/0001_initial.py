# Generated by Django 4.0.3 on 2022-04-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ful_name', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]
