# Generated by Django 2.2.3 on 2019-08-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0004_season_season_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='plot',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='season',
            name='season_name',
            field=models.TextField(default=None),
        ),
    ]
